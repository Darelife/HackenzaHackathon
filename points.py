import json
import requests
import time

# Btw, cuz of a small bug, not every prof has a points key in the json file...will need to run a separate script to fix it

with open("profsId.json") as f:
  ids = json.load(f)

with open("profsName.json") as f:
  names = json.load(f)

with open("formatted_conference.json") as f:
  confs = json.load(f)

with open("formatted_journal.json") as f:
  journals = json.load(f)

url = "https://dblp.org/search/publ/api/"
# in requests, we can pass the query as a dictionary
params = {
  # 'q': 'Arnab Kumar Paul',
  'format': 'json'
}

confsAccronyms = []
for i in confs:
  confsAccronyms.append(i["acronym"])

articles = {}
# Process the data as needed

# A. Akbari Azirani has 5.050000000000001 points
with open("articles.json", "r") as f:
    articlesDatai = json.load(f)
index = 0
for i in names:
  if (index <= len(articlesDatai)-1): index +=1; continue
  with open("break.json", "r") as f:
    breakData = json.load(f)

  # Got forced to do this cuz ctrl+c in the terminal gets delayed for some reason, and also ends up somehow deleting a chunk of the data
  if (breakData["break"] == 1): 
    breakData["break"] = 0
    with open("break.json", "w") as f:
      json.dump(breakData, f, indent=2)
    break
  if (breakData["breakIn"] > 0):
    breakData["breakIn"] -= 1
    with open("break.json", "w") as f:
      json.dump(breakData, f, indent=2)
  # print("working")
  if (breakData["breakIn"] == 0):
    breakData["breakIn"] = -1
    with open("break.json", "w") as f:
      json.dump(breakData, f, indent=2)
    break
  time1 = time.time()
  profArticles = []
  params['q'] = i
  with open("articles.json", "r") as f:
    articlesDatai = json.load(f)
  try:
    response = requests.get(url, params=params)
    data = response.json()
  except:
    print(f"Error with {url}?q={i}&format=json")
    continue
  point = 0
  # print("working")
  for j in data["result"]["hits"]["hit"]:
    articlesData = {}
    try:
      if j["info"]["type"] == "Conference and Workshop Papers":
        if j["info"]["venue"] in confsAccronyms:
          point += 1/(len(j["info"]["authors"]["author"]))
          articlesData['authors'] = j["info"]["authors"]["author"]
          articlesData['title'] = j["info"]["title"]
          articlesData['venue'] = j["info"]["venue"]
          articlesData['year'] = j["info"]["year"]
          articlesData['type'] = j["info"]["type"]
          articlesData['points'] = 1/(len(j["info"]["authors"]["author"]))
          articles[j["info"]["key"]] = articlesData
      elif j["info"]["type"] == "Journal Articles":
        if j["info"]["venue"] in journals:
          point += 1/(len(j["info"]["authors"]["author"]))
          articlesData['authors'] = j["info"]["authors"]["author"]
          articlesData['title'] = j["info"]["title"]
          articlesData['venue'] = j["info"]["venue"]
          articlesData['year'] = j["info"]["year"]
          articlesData['type'] = j["info"]["type"]
          articlesData['points'] = 1/(len(j["info"]["authors"]["author"]))
          articles[j["info"]["key"]] = articlesData
        else:
          url2 = f"https://dblp.org/search/venue/api/?q={j["info"]["venue"]}&format=json"
          try:
            time.sleep(1.75)
            response2 = requests.get(url2)
            data2 = response2.json()
          except:
            print(f"Error with {url2}")
            continue
          if int(data2["result"]["hits"]["@total"]) > 0:
            try:
              if (data2["result"]["hits"]["hit"][0]["info"]["venue"] in journals or data2["result"]["hits"]["hit"][1]["info"]["venue"] in journals):
                point += 1/(len(j["info"]["authors"]["author"]))
                articlesData['authors'] = j["info"]["authors"]["author"]
                articlesData['title'] = j["info"]["title"]
                articlesData['venue'] = j["info"]["venue"]
                articlesData['year'] = j["info"]["year"]
                articlesData['type'] = j["info"]["type"]
                articlesData['points'] = 1/(len(j["info"]["authors"]["author"]))
                articles[j["info"]["key"]] = articlesData
            except:
              try:
                time.sleep(1.75)
                if (data2["result"]["hits"]["hit"][0]["info"]["venue"] in journals):
                  point += 1/(len(j["info"]["authors"]["author"]))
                  articlesData['authors'] = j["info"]["authors"]["author"]
                  articlesData['title'] = j["info"]["title"]
                  articlesData['venue'] = j["info"]["venue"]
                  articlesData['year'] = j["info"]["year"]
                  articlesData['type'] = j["info"]["type"]
                  articlesData['points'] = 1/(len(j["info"]["authors"]["author"]))
                  articles[j["info"]["key"]] = articlesData
              except:
                print(f"Error with {url2}")
                continue
      time.sleep(1.75)
      # articlesDatai[i] = articlesData
      profArticles.append(articlesData)
    except:
      print(f"Error with {j}")
      continue
  # time.sleep(30)
  time2 = time.time()
  print(f"{i} took {time2-time1} seconds")

  names[i]["points"] = point
  # ids[index]["points"] = point
  print(f"{i} has {point} points")
  index += 1
  # articlesDatai.update(articles)
  articlesDatai[i] = profArticles
  with open("articles.json", "w") as f:
    json.dump(articlesDatai, f, indent=2)
  with open("profsName.json", "w") as f:
    json.dump(names, f, indent=2)

  # This is also like the breakIn thing, but it's predecided, and can't be changed when the program is running
  if (index == 100):
    break

with open("profsName.json", "w") as f:
  json.dump(names, f, indent=2)

# with open("profsId.json", "w") as f:
#   json.dump(ids, f, indent=2)
