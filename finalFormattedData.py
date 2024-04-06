import json

with open("indianArticles.json", "r") as f:
    articles = json.load(f)

with open("IndianProfs.json", "r") as f:
    profs = json.load(f)

with open("conferenceAcronyms.json", "r") as f:
    confsAccronyms = json.load(f)

websiteData = {}

for i in articles:
    for j in articles[i]:
        if j["year"] not in websiteData:
            websiteData[j["year"]] = []
        try:
            try:
                # if conference
                if j["venue"] in confsAccronyms:
                    websiteData[j["year"]].append(
                        {
                            "author": i,
                            "affiliation": profs[i]["affiliation"],
                            "points": j["points"],
                            "FOR": confsAccronyms[j["venue"]]["FOR"],
                        }
                    )
                # if journal
                else:
                    websiteData[j["year"]].append(
                        {
                            "author": i,
                            "affiliation": profs[i]["affiliation"],
                            "points": j["points"],
                            "FOR": "Journal",
                        }
                    )
            except:
                websiteData[j["year"]].append(
                    {
                        "author": i,
                        "affiliation": profs[i]["affiliation"],
                        "points": j["points"],
                        "FOR": "Journal",
                    }
                )
        except:
            print(f"Error with {i} - {j['venue']} - {j['year']}")
            continue

# Sort the websiteData by key of the dictionary
websiteData = dict(sorted(websiteData.items()), reverse=True)

with open("websiteData.json", "w") as f:
    json.dump(websiteData, f, indent=2)

print("Done")
