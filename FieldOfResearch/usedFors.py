import json

with open("E:\Programming\Hackathon\Hackenza\websiteData.json", "r") as f:
    websiteData = json.load(f)

x = []

for i in websiteData:
    try:
        for j in websiteData[i]:
            for k in j["FOR"]:
                if k not in x:
                    x.append(k)
    except:
        pass

with open("./FieldOfResearch/usedFors.json", "w") as f:
    json.dump(x, f, indent=4)
