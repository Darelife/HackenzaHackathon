import json

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
