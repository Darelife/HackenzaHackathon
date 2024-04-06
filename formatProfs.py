import pandas
import json

# use pandas to read the csv file
df = pandas.read_csv('profs.csv')

# create a dictionary to store the data
data = {}
data2 = {}
# iterate through the rows of the dataframe
# print the first row of df
print(df.iloc[0]['name'])
# print the length of the df
for i in range(len(df)):
  data[df.iloc[i]['scholarid']] = {
    'name': df.iloc[i]['name'],
    'affiliation': df.iloc[i]['affiliation'],
    'homepage': df.iloc[i]['homepage']
  }
  data2[df.iloc[i]['name']] = {
    'scholarid': df.iloc[i]['scholarid'],
    'affiliation': df.iloc[i]['affiliation'],
    'homepage': df.iloc[i]['homepage']
  }

# write the data to a json file
with open('profsId.json', 'w') as f:
  json.dump(data, f, indent=2)

with open('profsName.json', 'w') as f:
  json.dump(data2, f, indent=2)