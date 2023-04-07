import json

path = 'extras/old.json'


def add_to_list(facts):
    # Create an empty list to hold the new facts
    new_facts = []

    # Load the existing facts from the JSON file
    try:
        with open(path, "r") as json_file:
            existing_data = json.load(json_file)
    except:
        existing_data = {"facts": []}

    # Loop through the new facts
    for fact in facts:
        add_fact = fact["og_fact"]
        
        # Check if the new fact is already in the existing facts
        if add_fact not in existing_data["facts"]:
            # If not, append it to the new facts list and add it to the existing facts
            new_facts.append(add_fact)
            existing_data["facts"].append(add_fact)

    # Write the updated facts to the JSON file
    with open(path, 'w') as f:
        json.dump(existing_data, f)
