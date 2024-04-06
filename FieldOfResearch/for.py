# open for.txt
# format : 1234 text
# save in json : {1234: "text"}


import json

with open("for.txt", encoding="cp437") as f:
    data = f.readlines()

formattedData = {}
for i in data:
    i = i.split()
    # i = [1234, "textword1 textword2 ... textwordn (random stuff)"]
    # j = "textword1 textword2 ... textwordn"
    j = " ".join(i[1:])
    j.split("(")
    j = j.split("(")[0]
    # remove the last space
    j = j[:-1]
    formattedData[int(i[0])] = j
    # formattedData[int(i[0])] =

with open("for.json", "w") as f:
    json.dump(formattedData, f, indent=2)
