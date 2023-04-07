# import json
from base64 import b64decode
from pathlib import Path


def convert_to_image(response, idx):
    # DATA_DIR = Path.cwd() / "ai"
    # JSON_FILE = DATA_DIR / "data/generated_images.json"

    IMAGE_DIR = Path.cwd() / "assets/temp/images/generated_images"

    IMAGE_DIR.mkdir(parents=True, exist_ok=True)

    # with open(JSON_FILE, mode="r", encoding="utf-8") as file:
    #     response = json.load(file)

    for image_dict in response["data"]:
        image_data = b64decode(image_dict["b64_json"])
        image_file = IMAGE_DIR / f"generated_images-{idx}.png"
        with open(image_file, mode="wb") as png:
            png.write(image_data)