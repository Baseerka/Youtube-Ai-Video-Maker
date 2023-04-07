# Youtube-Ai-Video-Maker<a id="project-title"></a>

Create Youtube Videos Using OpenAI's API

With this code, you can create videos like [Link To The Video](https://youtube.com/shorts/WWt5XI1te14?feature=share)/You can find it in the sample folder if you want.

## Table of Contents

- [Project Title](#project-title)
- [How it works](#explanation)
- [Tutorials](#explanation)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## How it works<a id="explanation"></a>

1. Uses OpenAi's API to generate 20 facts using GPT-3.5 Turbo.
2. Filters the response dictionary to only include the facts and the prompt required to generate the images.
3. Checks for repetition of facts and eliminates them.
4. Converts the facts into audio files.
5. Downloads a background video and adjusts its length based on the audio.
6. Generates images using the prompts from the response.
7. Combines the audio, facts, and background into one video.
8. Keeps a record of used facts to avoid repetition in future videos.
9. Randomly selects a title, description, and tags from a pre-made dictionary.
10. Uses the above details to upload the video to YouTube.
11. Removes the used facts and generates a new video with the remaining facts.
12. Repeats the process until it runs out of facts.
13. You can run the program again to create new facts.

## Tutorials<a id="tutorials"></a>

1. How to make this code work:

<b>Coming soon</b>

2. How to take api file from youtube:

<b>Coming soon</b>

3. How to setup manual upload :

<b>Coming soon</b>

## Installation

1. Clone this repository: `git clone https://github.com/Baseerka/Youtube-Ai-Video-Maker.git`
2. Create a Python virtual environment (optional): `python -m venv env` and activate it `env\scripts\activate` (Windows) or `source env/bin/activate` (Linux/macOS).
3. Install the required dependencies: `pip install -r requirements.txt`
4. Type the OpenAI API key in `important/important.py`: `openai_api = "YOUR_API_KEY"`
5. Change the voice if needed in the same direcory `important/important.py` by going to `sample/audio/` directory you can find sample audio file to select which audio you want to select.
6. To automatically upload the video, add a YouTube API file to the main folder (tutorial to be updated soon).
7. Alternatively, to manually upload the video, add the path to the browser in `important/important.py`.

## Usage

The program uses OpenAI's API to take 20 facts from gpt-3.5-turbo. It then takes the response and only filters the dictionary which contains the facts and the prompt to generate our image. It takes the facts and checks if the fact was used in paste in order to stop the repetition of facts in videos. It takes the facts and changes them into audio files. It makes a background according to the audio length (downloads background video if it does not exist). It takes the image generation prompt from the response we got from the model - gpt-3.5-turbo and generates images for our facts (it will ask for your confirmation). It combines the audio, facts, and background into one. Add the existing facts to a dictionary so that they can check it later for future repetition. It takes random title, description, and tags from the premade dictionary and use them as video details. Use these details to upload the video to YouTube. The used facts are removed and a new video is made with the rest of the facts. This process is repeated until it runs out of facts. You can run the program again to create new facts.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes. We welcome contributions of all kinds, whether it's adding new features, fixing bugs, or improving documentation.

## Credits

- [elebumm/RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot) for the code to get the TTS and background.
- Inspired by [this video](https://youtu.be/CjHP1W3nxe8a).

Use this and modify it into a good one.
