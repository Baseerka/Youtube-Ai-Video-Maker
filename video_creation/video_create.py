import multiprocessing
import cv2

from moviepy.audio.AudioClip import concatenate_audioclips, CompositeAudioClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.VideoClip import ImageClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.compositing.concatenate import concatenate_videoclips
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.editor import TextClip
from rich.console import Console
from pathlib import Path

console = Console()


def prepare_background(background_path: str, dur, W: int, H: int) -> VideoFileClip:
    Path(f"assets/temp/{background_path}/").mkdir(parents=True, exist_ok=True)

    clip = (
        VideoFileClip(f"assets/temp/{background_path}/backgrounde.mp4")
        .without_audio()
        .resize(height=H)
        .subclip(0, dur)
    )

    # calculate the center of the background clip
    c = clip.w // 2

    # calculate the coordinates where to crop
    half_w = W // 2
    x1 = c - half_w
    x2 = c + half_w

    return clip.crop(x1=x1, y1=0, x2=x2, y2=H)
 

def make_final_video(facts):
    # settings values
    W = 1080
    H = 1920

    # try:  # if it isn't found (i.e you just updated and copied over config.toml) it will throw an error
    #    VOLUME_MULTIPLIER = settings.config["settings"]['background']["background_audio_volume"]
    # except (TypeError, KeyError):
    #    print('No background audio volume found in config.toml. Using default value of 1.')
    #    VOLUME_MULTIPLIER = 1

    print("Creating the final video 🎥")

    VideoFileClip.reW = lambda clip: clip.resize(width=W)
    VideoFileClip.reH = lambda clip: clip.resize(width=H)

    opacity = 1


    audio_clips = []
    for fact in facts:
        fact_audio = AudioFileClip(fact["audio_file"])
        audio_clips.append(fact_audio)
    audio_concat = concatenate_audioclips(audio_clips)
    audio_composite = CompositeAudioClip([audio_concat])

    # Gather all images
    new_opacity = 1 if opacity is None or float(opacity) >= 1 else float(opacity)
    image_height = int(H//2-200)

    image_clips = []
    for i, fact in enumerate(facts):
        image_clips.append(ImageClip(fact["image_path"])
            .set_duration(audio_clips[i].duration)
            .resize(width=image_height)
            .set_opacity(new_opacity)
            )

    image_concat = concatenate_videoclips(image_clips).set_position(("center", 70))
    # note transition kwarg for delay in imgs
    image_concat.audio = audio_composite

    # Iterate over the list of texts and add each text to the text_clip
    fact_clips = []
    current_time = 0
    for fact_cuts in facts:
        for fact in fact_cuts["facts_duration"]:
            text_clip = TextClip(fact['text'], font='fonts/Poppins-Black.ttf', fontsize=120, color='white', stroke_color='black', stroke_width=5)
            text_clip = text_clip.set_position("center",  H//2 - 50).set_duration(fact['duration']).set_start(current_time)	    
            # Create a list to hold the text clips
            fact_clips.append(text_clip)
            current_time += fact['duration']
    # fact_concat = concatenate_videoclips(fact_clips).set_position(
    #     img_clip_pos,  H//2 - 50
    # )
    background_clip = prepare_background("cropped_background", current_time, W=W, H=H)
    final = CompositeVideoClip([background_clip, image_concat] + fact_clips)
    
    Path("youtube/videos/").mkdir(parents=True, exist_ok=True)
    final.write_videofile(
        f"youtube/videos/final_video.mp4",
        fps=int(30),
        audio_codec="aac",
        audio_bitrate="192k",
        verbose=False,
        threads=multiprocessing.cpu_count(),
        #preset="ultrafast", # for testing purposes
    )