# get the data from CORE.csv, and format it to json format (only select the name, acronym, rating, field of research (FOR(1,2,3)))

import csv
import json

print('Formatting data...')

# read the data from CORE.csv
with open('CORE.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

# get the header of the data
header = data[0]

# get the index of the columns that we need
name_index = header.index('name')
acronym_index = header.index('acronym')
rating_index = header.index('rating')
# FOR1, FOR2, FOR3 are the fields of research (they may be empty)
FOR1_index = header.index('FOR1')
FOR2_index = header.index('FOR2')
FOR3_index = header.index('FOR3')

# create a list to store the formatted data
formatted_data = []

# iterate through the data

for row in data[1:]:
    # get the name, acronym, rating, and field of research
    name = row[name_index]
    acronym = row[acronym_index]
    rating = row[rating_index]
    FOR1 = row[FOR1_index]
    FOR2 = row[FOR2_index]
    FOR3 = row[FOR3_index]
    if (rating == 'A' or rating == 'A*'):
    # create a dictionary to store the formatted data
        formatted_row = {
            'name': name,
            'acronym': acronym,
            'rating': rating,
            'FOR': [FOR1, FOR2, FOR3]
        }

    # add the formatted data to the list
    formatted_data.append(formatted_row)

# write the formatted data to a json file
with open('formatted_conference.json', 'w') as f:
    json.dump(formatted_data, f, indent=4)

print('Data formatted successfully!')

# The formatted data is stored in formatted_conference.json
# The format is as follows:
# [
#     {
#         "name": "name",
#         "acronym": "acronym",
#         "rating": "rating",
#         "FOR": ["FOR1", "FOR2", "FOR3"]
#     },
#     ...
# ]