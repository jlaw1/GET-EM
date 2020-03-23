import json
import pandas as pd
import requests
import numpy as np

# postcodes =['P0L1B0','P5A3P1', 'P5A3P2', 'P5A3P3']
# results = []

# for postcode in postcodes:
#     res = requests.get('https://represent.opennorth.ca/postcodes/{}'.format(postcode))

#     if res.status_code == 200:
#         results.append(res.json())
#     else: 
#         print("Request to {} failed".format(postcode))

# match_id =['P0L1B0','P5A3P1', 'P5A3P2', 'P5A3P3']
# results = []

# for match_id in match_id:
#     res = requests.get("https://api.opendota.com/api/matches/{match_id}")
# requests.get('https://represent.opennorth.ca/postcodes/{}'.format(postcode))

#     if res.status_code == 200:
#         results.append(res.json())
#     else: 
#         print("Request to {} failed".format(postcode))


# https://api.opendota.com/api/matches/{match_id}

# Example: grand final game 4 
# 4986461644

# game 1, 2, 3, 4: ['4986133311', '4986260666', '4986362254', '4986461644']

match_id = ['4986133311', '4986260666', '4986362254', '4986461644']
results=[]
url = "https://api.opendota.com/api/matches/{match_id}"
results = requests.get(url).json()
# JSONContent = requests.get(url).json()
content = json.dumps(results, indent = 4, sort_keys=True)
print(content)


# import urllib.request, json  with
# urllib.request.urlopen("http://datdota.com/api/drafts?faction=both&first-pick=either&leagues=11280&tier=1&tier=2&valve-event=does-not-matter&after=01%2F01%2F2011&before=14%2F02%2F2020&duration=0%3B200&duration-value-from=0&duration-value-to=200")
# as url: data = json.loads(url.read().decode()) print(data)

# response = requests.get("http://datdota.com/api/drafts?default=true")



# response =
# requests.get("http://datdota.com/api/drafts?faction=both&first-pick=either&leagues=11280&tier=1&tier=2&valve-event=does-not-matter&after=01%2F01%2F2011&before=14%2F02%2F2020&duration=0%3B200&duration-value-from=0&duration-value-to=200")


print(response.status_code)
