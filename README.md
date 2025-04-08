# Youtube-Ai-Video-Maker<a id="project-title"></a>

Create Youtube Videos Using OpenAI's API

With this code, you can create videos like [Link To The Video](https://youtube.com/shorts/WWt5XI1te14?feature=share)/You can find it in the sample folder if you want.

## Table of Contents

- [Project Title](#project-title)
- [How it works](#explanation)
- [Tutorials](#tutorials)
- [Installation](#installation)
- [Requirements](#requirements)
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

### 1. How to make this code work:

  1. **Clone the Repository**: 
    Begin by cloning the project repository to your local machine:​
  
  ```bash
  git clone https://github.com/Baseerka/Youtube-Ai-Video-Maker.git
  ```
  
  2. **Set Up a Virtual Environment (Optional)**: 
    It's recommended to use a virtual environment to manage dependencies:​
  
  - For Windows:​
  
  ```bash
  python -m venv env
  env\Scripts\activate
  ```
  
  - For Linux/macOS:​
  
  ```bash
  python3 -m venv env
  source env/bin/activate
  ```
  
  3. **Install Required Dependencies**: 
     Navigate to the project directory and install the necessary packages:​
  
  ```bash
  cd Youtube-Ai-Video-Maker
  pip install -r requirements.txt
  ```
  
  4. **Configure the OpenAI API Key**: 
    Obtain your OpenAI API key from the OpenAI API page. Then, open the `important/important.py` file and set your API key:​
  
  ```python
  openai_api = "YOUR_API_KEY"
  ```
  
  5. **Select a Voice for Text-to-Speech (TTS)**: 
    The project includes sample audio files in the `sample/audio/ directory`. Choose a voice that suits your preference and update the `voice` variable in `important/important.py` accordingly:​
  
  ```python
  voice = "path_to_selected_voice_file"
  ```
  
  6. **Set Up YouTube API for Automatic Uploads (Optional)**: 
    To enable automatic video uploads to YouTube:​
  
      - Obtain your YouTube Data API credentials by following the [YouTube API documentation](https://developers.google.com/youtube/registering_an_application).​
      - Download the `client_secrets.json` file from the Google Cloud Console.​
      - Place the `client_secrets.json` file in the main project directory.​
  
  7. **Configure Manual Upload (Alternative to Automatic Uploads)**:
     If you prefer to upload videos manually:​
  
      - Open the `important/important.py` file.​
      - Set the `manual_upload` variable to True.​
      - Specify the path to your web browser's executable in the `browser_path` variable. For example:​
  
  ```python
  manual_upload = True
  browser_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
  ```
  
  8. **Run the Main Script**: 
    With all configurations in place, execute the main script to start the video creation process:​

```bash
python main.py
```

### 2. How to take api file from youtube:

   - Visit the [Google Developer Console](https://console.developers.google.com/)
   - Create a project or use an existing one.
   - Enable the **YouTube Data API v3**.
   - Create OAuth 2.0 credentials (Desktop App) and download the JSON file.
   - Save it and update the `credentials_file` path in `config.json`.

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

## Requirements <a id="requirements"></a>

1. Take api key from [OpenAI API](https://platform.openai.com/account/api-keys)

## Usage

The program uses OpenAI's API to take 20 facts from gpt-3.5-turbo. It then takes the response and only filters the dictionary which contains the facts and the prompt to generate our image. It takes the facts and checks if the fact was used in paste in order to stop the repetition of facts in videos. It takes the facts and changes them into audio files. It makes a background according to the audio length (downloads background video if it does not exist). It takes the image generation prompt from the response we got from the model - gpt-3.5-turbo and generates images for our facts (it will ask for your confirmation). It combines the audio, facts, and background into one. Add the existing facts to a dictionary so that they can check it later for future repetition. It takes random title, description, and tags from the premade dictionary and use them as video details. Use these details to upload the video to YouTube. The used facts are removed and a new video is made with the rest of the facts. This process is repeated until it runs out of facts. You can run the program again to create new facts.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes. We welcome contributions of all kinds, whether it's adding new features, fixing bugs, or improving documentation.

## Credits

- [elebumm/RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot) for the code to get the TTS and background.
- Inspired by [this video](https://youtu.be/CjHP1W3nxe8a).
- [Tutorials Point](https://www.tutorialspoint.com/program-to-check-whether-two-sentences-are-similar-or-not-in-python) for the code to check if we used it in the past(I searched for it everywhere but nothing worked like their code🤯🤯).

Use this and modify it into a good one.
