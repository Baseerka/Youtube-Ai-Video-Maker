from important.important import openai_api
from ai.image_converter import convert_to_image
from ai.pick_all_image import multi_img
from pathlib import Path

import openai
import json, os

# # # Set your OpenAI API key
openai.api_key = openai_api

def image_generator(prompts):
    image_paths = []
    for idx, prompt in enumerate(prompts):
        prompt = prompt["image_prompt"]
        time = 0
        sure = ""
        indx = 0
        while sure.lower() != "no" and sure.lower() != "n":
            # Set the prompt
            prompt = prompt

            # Set the model and image parameters
            model = "image-alpha-001"
            image_size = "1024x1024"

            # Set the number of images to generate
            num_images_to_generate = 1

            # Generate the images using OpenAI's DALL-E API
            response = openai.Image.create(
                prompt=prompt,
                n=num_images_to_generate,
                size=image_size,
                model=model,
                response_format="b64_json",
            )

            Path("ai/data/").mkdir(parents=True, exist_ok=True)

            file_name = "ai/data/generated_images.json"
            
            with open(file_name, mode="w", encoding="utf-8") as file:
                json.dump(response, file)

            # file_name = "ai/data/generated_images.json"
            # with open(file_name, mode="r", encoding="utf-8") as file:
            #     response = json.load(file)

            if sure.lower() == "c" or sure.lower() == "change":
                convert_to_image(response, indx)
            else:
                convert_to_image(response, 0)
            
            indx += 1

            print(prompt)
            path, sure = multi_img(idx, time)
            if path is not None:
                image_paths.append(path)

        gen_img_path = "assets/temp/images/generated_images/"
        for file in os.listdir(gen_img_path):
            os.remove(gen_img_path + file)
    
    return image_paths
