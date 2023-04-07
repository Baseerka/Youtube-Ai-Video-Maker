import re
from pathlib import Path
from typing import Tuple
from moviepy.editor import AudioFileClip
from rich.progress import track
from voice.sanitize import sanitize_text
DEFAULT_MAX_LENGTH: int = 50 # video length variable


class TTSEngine:

    def __init__(
        self,
        tts_module,
        facts: dict,
        path: str = "assets/temp/",
        max_length: int = DEFAULT_MAX_LENGTH,
        last_clip_length: int = 0,
    ):
        self.tts_module = tts_module()
        self.facts = facts

        self.factid = re.sub(r"[^\w\s-]", "", "audio")
        self.path = path + self.factid
        self.max_length = max_length
        self.length = 0
        self.last_clip_length = last_clip_length

    def add_periods(self):  # adds periods to the end of paragraphs (where people often forget to put them) so tts doesn't blend sentences
        for fact in self.facts:
            fact["fact"] = fact["fact"].replace('\n', '. ')
            if fact["fact"][-1] != '.': 
                fact["fact"] += '.' 

    def run(self) -> Tuple[int, int]:

        Path(f"{self.path}/mp3").mkdir(parents=True, exist_ok=True)
        Path(f"{self.path}/final").mkdir(parents=True, exist_ok=True)
        print("Saving Text to MP3 files...")
	
        self.add_periods()
        idx = None
        facts = []
        for idx, fact in track(
            enumerate(self.facts), "Saving..."
        ):
            # ! Stop creating mp3 files if the length is greater than max length.
            if self.length > self.max_length and idx > 1:
                self.length -= self.last_clip_length
                idx -= 1
                break
            facts_duration = self.duration_per_text(fact)
            final_audio_name = f"{self.path}/final/final_audio{idx}.mp3"
            self.call_tts_final(f"{final_audio_name}", process_text(fact["fact"]))
            all = {}
            all["facts_duration"] = facts_duration
            all["audio_file"] = final_audio_name
            all["image_prompt"] = fact["topic"]
            all["id"] = idx
            all["og_fact"] = fact['fact']
            facts.append(all)
                    

        print("Saved Text to MP3 files successfully.")
        return self.length, idx, facts

    def duration_per_text(self, fact, max_chars=14):
        durations_fact = []
        lines = []
        audio_clips = []
        audios = 0
        temp_audio = []
        for line in fact["fact"].split(" "):
            lines.append(line)
            if len(" ".join(lines)) > max_chars:
                lines.pop()
                audios += 1
                text = " ".join(lines)
                self.call_tts(f"{audios}", process_text(text))
                lines = []
                lines.append(line)
                temp_audio.append(f"{self.path}/mp3/{audios}.mp3")
                try:
                    clip = AudioFileClip(f"{self.path}/mp3/{audios}.mp3")
                    all = {}
                    all["duration"] = clip.duration - 0.3
                    all["text"] = text
                    durations_fact.append(all)
                    audio_clips.append(clip)
                except:
                    self.length = 0
        if lines:
            text = " ".join(lines)
            self.call_tts(f"{audios + 1}", process_text(text))
            temp_audio.append(f"{self.path}/mp3/{audios}.mp3")
            try:
                clip = AudioFileClip(f"{self.path}/mp3/{audios + 1}.mp3")
                all = {}
                all["duration"] = clip.duration
                all["text"] = text
                durations_fact.append(all)
                audio_clips.append(clip)
            except:
                self.length = 0
        
        return durations_fact

    def call_tts(self, filename: str, text: str):
        self.tts_module.run(text, filepath=f"{self.path}/mp3/{filename}.mp3")
        try:
            clip = AudioFileClip(f"{self.path}/mp3/{filename}.mp3")
            self.last_clip_length = clip.duration
            self.length += clip.duration
            clip.close()
        except:
            self.length = 0

    def call_tts_final(self, filename: str, text: str):
        self.tts_module.run(text, filepath=filename)
        try:
            clip = AudioFileClip(filename)
            self.last_clip_length = clip.duration
            self.length += clip.duration
            clip.close()
        except:
            self.length = 0

def process_text(text: str , clean : bool = True):
    new_text = sanitize_text(text) if clean else text
    return new_text
