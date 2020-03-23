import requests
import json
import time
import csv
#pandas as pd


# Get picks_bans in order in oneline

# match_id list for event/league
input_file = open('opendota_matches/match_list/league_id_10979_starladder_s2.json') 
matches = json.load(input_file) # !! LIST OF MATCH_ID's FOR THE EVENT
input_file.close()
print('Loading {} matches\n'.format(len(matches)))


matchdata = open('opendota_matches/matches/league_id_10979_starladder_s2_matchdata.json') 
data = json.load(matchdata)
matchdata.close()

# matchdata = open('opendota_matches/matches/league_id_11371_summit_11_matchdata_2.json')
# data = json.load(matchdata) # !! MATCH DATA PULLED FROM OPENDOTA
# matchdata.close()

# GO THROUGH MATCH DATA AND EXTRACT PICKS_BANS FEATURE AND WRITE PICKS_BANS DATA INTO 1 LINE PER MATCH
# Nested loop at end should give me 'picks_bans' data in a single line formatted as:
	# "Match details", + 1is_pick, 1team, 1hero_id, 2is_pick,...

with open('picks_bans/leagueid_10979_starladder_picks_bans.csv', 'w') as picks: # Open 
	for m in matches:
		curmatch = data['m']['picks']
		#match_id = curmatch['match_id']
		# lastseqnum = curmatch['match_seq_num']
		#print(str(i + 1) + "/100 " + str(match_id))
		#print(str(match_id))
		if 'picks_bans' in curmatch: 
			print( 'm' + str(match_id))
			picks.write(str(match_id) + ",") # match_id
			picks.write(str(dire_team_id) + ",") # team playing on dire side 
			picks.write(str(radiant_team_id) + ",") # team playin on radiant side
			picks.write(str(curmatch['radiant_win']) + ",") # match result 
			picks.write(str(curmatch['duration'])) # length of match 
			picklist = curmatch['picks_bans'] # define picks_bans feature as 'picklist'
			for i in range(len(picklist)):
				picks.write("," + str(picklist[i]['is_pick']) + "," + str(picklist[i]['team']) + "," + str(picklist[i]['hero_id'])) 
			matches.write("\n")
close()

#[m['match_id']] # NOT SURE IF SETTING UP THIS PART CORRECT 
#['result']['matches'][m] 
#data.format(m['match_id'].
# # 'dire_team_id',
# # 'leagueid'
# # 'radiant_team_id',
# # 'start_time',
# # 'series_id',
#  'series_type',
	

# 	data = accessMatchHistory(lastseqnum)
# 	for i in range(100):
# 		curmatch = data['result']['matches'][i]
# 		match_id = curmatch['match_id']
# 		lastseqnum = curmatch['match_seq_num']
# 		print(str(i + 1) + "/100 " + str(match_id))
# 		if 'picks_bans' in curmatch:
# 			print(str(match_id) + " captain's mode")
# 			matches.write(str(match_id) + ",")
# 			matches.write(str(curmatch['radiant_win']) + ",")
# 			matches.write(str(curmatch['duration']))
# 			picklist = curmatch['picks_bans']
# 			for i in range(len(picklist)):
# 				matches.write("," + str(picklist[i]['is_pick']) + "," + str(picklist[i]['team']) + "," + str(picklist[i]['hero_id']))
# 			matches.write("\n")
# 	matches.close()
# 	# if any error occured before this point it must have occured at "lastseqnum"


# # original 
# # reference: https://github.com/jlaw1/dota2drafts/blob/master/httprequest.py

# matches = open('./testing/data.csv', 'a') # Open 
# 	data = accessMatchHistory(lastseqnum)
# 	for i in range(100):
# 		curmatch = data['result']['matches'][i]
# 		match_id = curmatch['match_id']
# 		lastseqnum = curmatch['match_seq_num']
# 		print(str(i + 1) + "/100 " + str(match_id))
# 		if 'picks_bans' in curmatch:
# 			print(str(match_id) + " captain's mode")
# 			matches.write(str(match_id) + ",")
# 			matches.write(str(curmatch['radiant_win']) + ",")
# 			matches.write(str(curmatch['duration']))
# 			picklist = curmatch['picks_bans']
# 			for i in range(len(picklist)):
# 				matches.write("," + str(picklist[i]['is_pick']) + "," + str(picklist[i]['team']) + "," + str(picklist[i]['hero_id']))
# 			matches.write("\n")
# 	matches.close()
# 	# if any error occured before this point it must have occured at "lastseqnum"
