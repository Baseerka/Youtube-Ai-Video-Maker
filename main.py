from ai.get_facts_with_title import get_facts
from voice.voices import save_text_to_mp3
from background.download_background import get_background_config, download_background, chop_background_video
from ai.get_ai_images import image_generator
from video_creation.video_create import make_final_video
from extras.adds_to_list import add_to_list
from extras.checks_if_exists import check_if_exists
from youtube.upload_video import upload_video
from youtube.upload_error import upload_errorr
from extras.cleanup import remove

import random
import math, json, time

def main():
    facts = get_facts()
    #Use in case of any error while running (To save some creds on OpenAI :)
    # with open("ai/data/generated_facts.json")as data:
    #     facts = json.load(data)
    factse = check_if_exists(facts)
    while facts["facts"] != []:
        length, number_of_facts, factes = save_text_to_mp3(factse)
        length = math.ceil(length)
        bg_config = get_background_config()
        download_background(bg_config)
        chop_background_video(bg_config, length)
        image_paths = image_generator(factes)
        for idx, add_image in enumerate(factes):
            add_image["image_path"] = image_paths[idx]
        make_final_video(factes)
        add_to_list(factes)
        youtube_details_path = "youtube/youtube.json"
        with open(youtube_details_path, "r") as details:
            details = json.load(details)
        random_title = random.choice(details['title'])
        random_descriptions = random.choice(details['descriptions'])
        random_tags = random.sample(details['tags'], 10)
        random_tags = ",".join(random_tags)
        video_data = {
        "file": "youtube/videos/final_video.mp4",
        "title":  f"{random_title}",
        "description": f"{random_descriptions}",
        "keywords": f"{random_tags}",
        "privacyStatus":"public"
        }
        print("Posting Video in 10 sec...")
        time.sleep(10)
        try:
            upload_video(video_data)
        except:
            upload_errorr(video_data)
        del facts["facts"][:number_of_facts]
        remove()

if __name__ == '__main__':
    main()