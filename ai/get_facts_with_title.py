import openai
from important.important import openai_api, prompt
from ai.json_converter import find_json, get_facts_json

openai.api_key = openai_api

def get_facts():
    messages = []
    system_msg = "You are a helpful assistant who helps me to create a youtube video about facts."
    messages.append({"role": "system", "content": system_msg})

    print("Creating facts...")
    message = prompt
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    #Saves in case of error
    get_facts_json(reply)
    #takes dictionary from the given result
    reply = find_json(reply)
    print(reply)
    return reply