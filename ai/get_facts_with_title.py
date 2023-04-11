import openai, json
from important.important import openai_api, prompt
from ai.json_converter import find_json, get_facts_json

openai.api_key = openai_api

with open("extras/old.json", "r") as old_facts:
    old_fact = json.load(old_facts)
    old_fact = "\n".join(old_fact['facts'])

def get_facts():
    messages = []
    system_msg = "You are a helpful assistant who helps me to create a youtube video about facts."
    messages.append({"role": "system", "content": system_msg})
    old_facts = f"previous facts are \n {old_fact}"
    messages.append({"role": "assistant", "content": old_facts})

    print("Creating facts...")
    message = prompt
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    with open("ai/data/raw.txt", "w") as text:
        text.write(reply)
    #Saves in case of error
    get_facts_json(reply)
    reply = find_json(reply)
    print(reply)
    return reply