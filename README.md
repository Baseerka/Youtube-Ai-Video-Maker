# Youtube-Ai-Video-Maker


# Create Youtube Videos Using OpenAI's API

With this code, you can create videos like [Link To The Video](https://youtube.com/shorts/WWt5XI1te14?feature=share)/You can find it in the sample folder if you want.## How it works

1 - Uses OpenAi's API to take 20 facts from gpt-3.5-turbo.  

2- It takes the response and only filters the dictionary which contains the facts and the prompt to generate our image.  

3 - It takes the facts and checks if the fact was used in paste in order to stop the repetition of facts in videos.  

4 - It takes the facts and changes them into audio files.  

5 - Makes a background according to the audio length(Downloads background video if it does not exist).  

6 - Takes the image generation prompt from the response we got from the model - gpt-3.5-turbo and generates images for our facts(It will ask for your confirmation).  

7 - Combines the audio, facts and background into one Example : [Link To The Video](https://youtube.com/shorts/WWt5XI1te14?feature=share)/You can find it in the sample folder if you want.  

8 - Add the existing facts to a dictionary so that they can check it later for future repetition.  

9 - Takes random title, description and tags from the premade dictionary and make it as use them as video details.  

10 - Use these details to upload the video to youtube.  

11 - The used facts are removed and makes a new video with the rest of the facts.  

12 - This process is repeated until it runs out of facts.  

13 - You can run the program again to create new facts
## How to run it.

If you want to run the code either download the code or clone it. 

```git clone https://github.com/Baseerka/Youtube-Ai-Video-Maker.git```

then open the code and create an environment(Not necessary).

```python -m venv env```

run this if you have created an environment 

```env\scripts\activate```

then run 

```pip install -r requirements.txt```

Now all the necessary things have been done.

Now type the OpenAi's API key in important/important.py 
openai_api = "YOUR_API_KEY"

You can change the voice if you want you can find how the voice sounds by going into sample/audio/ then finding and typing the audio's name that you like.

After that is done if you want to automatically upload you have to add a youtube API file to the main folder.

Tutorial to get it will be updated soon...

Or you can use the manual uploading option to you this you have to add the path to the browser in important.

The tutorial to do that will be updated soon...



## Special thx to

https://github.com/elebumm/RedditVideoMakerBot for the code to get The TTS and Background.

Took the idea about making this video from https://youtu.be/CjHP1W3nxe8a
