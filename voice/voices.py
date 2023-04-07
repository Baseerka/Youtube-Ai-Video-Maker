from rich.console import Console

from voice.TTS.engine_wrapper import TTSEngine
from voice.TTS.streamlabs_polly import StreamlabsPolly

console = Console()

#Can add more TTS if wanted
TTSProviders = {
    "StreamlabsPolly": StreamlabsPolly,
}
TTSProvider = ["StreamlabsPolly"]

def save_text_to_mp3(facts):

    while True:
        # print("Please choose one of the following TTS providers: ")
        # print(TTSProvider)
        choice = "StreamlabsPolly"#input("\n")
        if choice.casefold() in map(lambda _: _.casefold(), TTSProviders):
            break
        print("Unknown Choice")
    text_to_mp3 = TTSEngine(
        get_case_insensitive_key_value(TTSProviders, choice), facts
    )
    return text_to_mp3.run()


def get_case_insensitive_key_value(input_dict, key):
    return next(
        (
            value
            for dict_key, value in input_dict.items()
            if dict_key.lower() == key.lower()
        ),
        None,
    )