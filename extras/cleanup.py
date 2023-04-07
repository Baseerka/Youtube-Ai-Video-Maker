import os

def remove():
    for files in os.listdir("assets/temp/audio/mp3"):
        os.remove(f"assets/temp/audio/mp3/{files}")
    for files in os.listdir("assets/temp/audio/final"):
        os.remove(f"assets/temp/audio/final/{files}")
    for files in os.listdir("assets/temp/cropped_background"):
        os.remove(f"assets/temp/cropped_background/{files}")