import requests
import json
import time
# league_id_10826_epicenter_2019.json
# Pull league_id_10826_epicenter_2019.json matches

# !! Patch 7.22 DPC tournament matches online/offline, by league_id 
# 1. match_list/league_id_10749_ti9.json
# 2. match_list/league_id_10979_starladder_s2.json
# 3. match_list/league_id_10826_epicenter_2019.json
# 4. match_list/league_id_11280_chengdu.json
# 5. match_list/league_id_11371_summit_11.json

# 1. league_id_10749_ti9_matchdata.json
# 2. league_id_10979_starladder_s2_matchdata.json
# 3. league_id_10826_epicenter_2019_matchdata.json
# 4. league_id_11280_chengdu_matchdata.json
# 5. league_id_11371_summit_11_matchdata.json

input_file = open('match_list/league_id_11280_chengdu.json') 
matches = json.load(input_file)
input_file.close()
print('Loading {} matches\n'.format(len(matches)))

# test once without the .format part. 
# Seem to get double of first match in list on occasion, may be duplicate due to re-make? or...
# I think you set i=1 instead of i=0, otherwise you get a double print of first match 

f = open('Patch_722_matchdata/league_id_11280_chengdu_matchdata.json', 'w')
i = 0 
for m in matches:
	print('requesting match {}'.format(m['match_id']))
	r = requests.get('https://api.opendota.com/api/matches/{}'.format(m['match_id']))
	f.write(r.text)
	f.write('\n')
	f.write(r.text)
	print(r.text)
	time.sleep(5)
	i += 1

print('processed {} matches'.format(i))
f.close()
