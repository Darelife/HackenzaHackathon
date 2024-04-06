import json

with open("IndianProfs.json", "r") as f:
  data = json.load(f)

print(len(data))