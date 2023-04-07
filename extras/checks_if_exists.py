import json
from pathlib import Path

path = "extras/old.json"

Path(path).mkdir(parents=True, exist_ok=True)

with open(path, "r") as f:
    result = json.load(f)

def check_if_exists(facts):
    new_facts = []
    if result:
        for fact in facts["facts"]:
            if fact["fact"] in result["facts"]:
                continue
            else:
                all = {}
                all["fact"] = fact["fact"]
                all["topic"] = fact["topic"]
                new_facts.append(all)
    return new_facts