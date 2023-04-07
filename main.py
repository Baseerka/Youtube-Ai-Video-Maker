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

from important.important import auto_upload, manual_upload, browser_data_dir, browser_exe_path

import math, json, time, os, random

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
        if not auto_upload:
            auto_upload_ask = ""
            while auto_upload_ask != "yes" and auto_upload_ask != "no" and auto_upload_ask != "y" and auto_upload_ask != "n":
                auto_upload_ask = input("Want to use automatic upload using Youtube api? yes(y)/no(n)")
                if auto_upload_ask == "yes" or auto_upload_ask == "y":
                    auto_upload = True
                elif auto_upload_ask == "no" or auto_upload_ask == "n":
                    auto_upload = False
                else: 
                    print("Unknown command")
        if auto_upload:
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
            for root, dirs, files in os.walk("./"):
                if "client_secrets.json" in files:            
                    try:
                        upload_video(video_data)
                    except:
                        if manual_upload:
                            if browser_exe_path != "" and browser_data_dir != "":
                                upload_errorr(video_data)
                            else:
                                print("you can find the video at 'youtube/videos'")
                                option = True
                else:
                    print('File to the youtube api is not found')
                    print("you can find the video at 'youtube/videos'")
                    option = True
        if option:
            input("Type any key after uploading the file or else you will loose the video file")
        del factse[:number_of_facts]
        remove()

if __name__ == '__main__':
    main()