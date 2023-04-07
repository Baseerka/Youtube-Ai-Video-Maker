import json
from pathlib import Path

def get_facts_json(facts):
    text = facts

    # Find a JSON string or a dictionary string in the text
    json_dict = find_json(text)

    # If a dictionary was found, append it to a JSON file
    path = "ai/data/generated_facts.json"

    Path(path).mkdir(parents=True, exist_ok=True)

    if json_dict:
        try:
            with open(path, "w") as json_file:
                json.dump(json_dict, json_file)
            print("JSON data written to file:", path)
        except Exception as e:
            print("Error writing JSON to file:", e)


# Define a function to find a JSON string or a dictionary string in a text
def find_json(text):
    start = text.find("{") # Find the start of a JSON string
    if start == -1:  # If not found, return None
        return None
    end = text.rfind("}") + 1  # Find the end of the JSON string
    if end == 0:  # If not found, return None
        return None
    json_str = text[start:end]  # Extract the JSON string
    try:
        json_dict = json.loads(json_str)  # Try to load the string as a dictionary
    except:
        return None  # If the string is not valid JSON, return None
    return json_dict  # Return the dictionary