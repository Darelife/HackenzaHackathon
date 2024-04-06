import json

with open("formatted_conference.json") as f:
    confs = json.load(f)

# save it as a dict -> key = acronym, value = everything else in dict

confsAcronyms = {}
for i in confs:
    confsAcronyms[i["acronym"]] = i

with open("conferenceAcronyms.json", "w") as f:
    json.dump(confsAcronyms, f, indent=2)
