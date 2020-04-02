import requests
import json
import time

# !! Patch 7.22 DPC tournament matches online/offline, by league_id 
# Inputs
# 1. data/league_id_10979_starladder_s2.json
# 2. data/league_id_10826_epicenter_2019.json
# 3. data/league_id_10749_ti9.json
# 4. data/league_id_11371_summit_11.json
# 5. data/league_id_11280_chengdu.json

# Outputs
# 1. data/league_id_10979_starladder_s2_matchdata.json
# 2. data/league_id_10826_epicenter_2019_matchdata.json
# 3. data/league_id_10749_ti9_matchdata.json 
# 4. data/league_id_11371_summit_11_matchdata.json
# 5. data/league_id_11280_chengdu_matchdata.json

input_file = open('data/league_id_11371_summit_11.json') 
matches = json.load(input_file)
input_file.close()
print('Loading {} matches\n'.format(len(matches)))

url = 'https://api.opendota.com/api/matches/{}'
params = {"api_key": ""}
# r = requests.get('https://api.opendota.com/api/matches/{}? + api_url'.format(m['match_id']))
responses = list()

for m in matches:
    print('requseting match {}'.format(m['match_id']))
    r = requests.get(url.format(m['match_id']), params=params)
    data = json.loads(r.text)
    responses.append(data)
    #api_data.update({m: data})
    print(data)

with open('data/league_id_11371_summit_11_matchdata.json', 'w') as data_file:
	json.dump(responses, data_file, indent=2)