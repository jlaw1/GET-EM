## Test 
## source
## https://medium.com/@waprin/python-and-dota2-analyzing-team-liquids-io-success-and-failure-7d44cc5979b2

import json
import time
import requests

## chengdu matchdata

input_file = open('match_list/league_id_11280_chengdu.json') 
matches = json.load(input_file)
input_file.close()
print('Loading {} matches\n'.format(len(matches)))

f = open('chengdu_11280_matchdata.txt', 'w')
i = 0 
for m in matches:
  print('requseting match {}'.format(m['match_id']))
  r = requests.get('https://api.opendota.com/api/matches/{}'.format(m['match_id']))
  f.write(r.text)
  f.write('\n')
  print(r.text)
  time.sleep(5)
  i += 1
  
print('processed {} matches'.format(i))
f.close()