import json
from pathlib import Path

path = "extras/old.json"

Path(path).mkdir(parents=True, exist_ok=True)

with open(path, "r") as f:
    result = json.load(f)

def check_if_exists(facts):
    new_facts = []
    for fact in facts["facts"]:
        for result in result["facts"]:
            if solve(fact["fact"], result):
                continue
        else:
            all = {}
            all["fact"] = fact["fact"]
            all["topic"] = fact["topic"]
            new_facts.append(all)
    return new_facts

def solve(s, t):
   s1 = s.split()
   s2 = t.split()
   if len(s1) > len(s2):
      s1,s2 = s2,s1
   while(s1):
      if(s2[0]==s1[0]):
         s2.pop(0)
         s1.pop(0)
      elif(s2[-1]==s1[-1]):
         s2.pop()
         s1.pop()
      else:
         return(False)
   return(True)