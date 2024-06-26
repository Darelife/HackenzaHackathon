import json

with open("indianArticles.json", "r") as f:
    articles = json.load(f)

with open("IndianProfs.json", "r") as f:
    profs = json.load(f)

with open("conferenceAcronyms.json", "r") as f:
    confsAccronyms = json.load(f)

with open("./FieldOfResearch/for.json", "r") as f:
    forData = json.load(f)

websiteData = {}

for i in articles:
    for j in articles[i]:
        if j["year"] not in websiteData:
            websiteData[j["year"]] = []
        try:
            try:
                # if conference

                if j["venue"] in confsAccronyms:
                    forr = []
                    for k in confsAccronyms[j["venue"]]["FOR"]:
                        try:
                            forr.append(forData[k])
                        except:
                            pass
                    websiteData[j["year"]].append(
                        {
                            "author": i,
                            "affiliation": profs[i]["affiliation"],
                            "points": j["points"],
                            "FOR": forr,
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


with open("websiteData.json", "r") as f:
    websiteData = json.load(f)

"""
New file structure:

{
    "year": {
        "affiliation" : {
            "points": 12.3,
            "faculty": 52,
            "articles": [
                {
                    "author": "author",
                    "points": "points",
                    "FOR": "FOR"
                },
                ...
            ]
        }
        ...
    },
    ...
}
"""

newWebsiteData = {}

flag = 1
for year in websiteData:
    newWebsiteData[year] = {}
    try:
        for article in websiteData[year]:
            if article["affiliation"] not in newWebsiteData[year]:
                newWebsiteData[year][article["affiliation"]] = {
                    "articles": [],
                    "points": 0,
                    "faculty": 0,
                }
            newWebsiteData[year][article["affiliation"]]["articles"].append(
                {
                    "author": article["author"],
                    "points": article["points"],
                    "FOR": article["FOR"],
                }
            )
            newWebsiteData[year][article["affiliation"]]["points"] = (
                newWebsiteData[year][article["affiliation"]]["points"] ** 2
                + article["points"]
            ) ** (1 / 2)
            newWebsiteData[year][article["affiliation"]]["faculty"] += 1

    except:
        # If there is an error, print the actual error statement and continue
        print(f"Error with {year} - {article['affiliation']}")
        continue

with open("websiteDataYear.json", "w") as f:
    json.dump(newWebsiteData, f, indent=4)


"""
{
    "affiliation" : {
        "points": 12.3,
        "faculty": 52,
        "years": {
            "year": [
                {
                    "author": "author",
                    "points": "points",
                    "FOR": "FOR"
                },
                ...
            ]
        }
    }
}
"""

newWebsiteDataAffiliation = {}

for year in newWebsiteData:
    for affiliation in newWebsiteData[year]:
        if affiliation not in newWebsiteDataAffiliation:
            newWebsiteDataAffiliation[affiliation] = {
                "points": 0,
                "faculty": 0,
                "years": {},
            }
        newWebsiteDataAffiliation[affiliation]["points"] += newWebsiteData[year][
            affiliation
        ]["points"]
        newWebsiteDataAffiliation[affiliation]["faculty"] += newWebsiteData[year][
            affiliation
        ]["faculty"]
        newWebsiteDataAffiliation[affiliation]["years"][year] = newWebsiteData[year][
            affiliation
        ]["articles"]

# sort the newWebsiteDataAffiliation by points
newWebsiteDataAffiliation = dict(
    sorted(
        newWebsiteDataAffiliation.items(),
        key=lambda x: x[1]["points"],
        reverse=True,
    )
)

with open("websiteDataAffiliation.json", "w") as f:
    json.dump(newWebsiteDataAffiliation, f, indent=4)


print("Done")
