import json

with open("profsName.json", "r") as f:
  data = json.load(f)

data2 = {}

key = ["IIT ", "IIIT ", "National Institute Of Technology", "BITS ", "IISc ", "ISI ", "Tata Inst"]
for i in data:
  for k in key:
    if (k in data[i]["affiliation"] or data[i]["affiliation"] == "CMI" or data[i]["affiliation"] == "IMSc"):
      data2[i] = data[i]

with open("IndianProfs.json", "w") as f:
  json.dump(data2, f, indent=2)