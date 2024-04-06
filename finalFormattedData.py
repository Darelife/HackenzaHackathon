import json

with open("indianArticles.json", "r") as f:
  data = json.load(f)

data2 = {}

for i in data:
  for j in data[i]:
    if j["year"] not in data2:
      data2[j["year"]] = []
    data2[j["year"]].append(
      {
        "author":i,
        "points":j["points"]
      }
    )

