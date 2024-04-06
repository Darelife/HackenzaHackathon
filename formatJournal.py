import csv
import json

# read the data from scimagojr.csv
with open('journals.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

# get the header of the data
header = data[0]

# get the index of the columns that we need
# coverage_index = header.index('coverage')
title_index = header.index('Title')
categories_index = header.index('Categories')
publisher_index = header.index('Publisher')
areas_index = header.index('Areas')

# create a list to store the formatted data
formatted_data = []

# iterate through the data
for row in data[1:]:
    # get the title, categories, and publisher
    # coverage = row[coverage_index]
    title = row[title_index]
    categories = row[categories_index]
    publisher = row[publisher_index]
    areas = row[areas_index]

    if 'Q1' in categories and 'Computer Science' in areas:
    # create a dictionary to store the formatted data
      formatted_row = {
          'title': title,
          'categories': categories,
          'publisher': publisher,
          'areas': areas
      }

    # add the formatted data to the list
      formatted_data.append(formatted_row)

# write the formatted data to a json file
with open('formatted_journal.json', 'w') as f:
    json.dump(formatted_data, f, indent=4)

print('Data formatted successfully!')
