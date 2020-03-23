# semi-modified version of picks_ban parse in json 

# list of match_id's for the event

input_file = open('opendota_matches/match_list/league_id_10979_starladder_s2.json') 
matches = json.load(input_file) # !! list of match_id's for given event
input_file.close()

# JSON file with match data from get request
with open('opendota_matches/matches/league_id_10979_starladder_s2_matchdata.json', 'r') as matchdata:
    JSONcontent = json.load(matchdata) # matchdata now deserialized json object 
#matchdata.close()

data = json_normalize(JSONcontent) #json object --> table 


# GO THROUGH MATCH DATA AND EXTRACT PICKS_BANS FEATURE AND WRITE PICKS_BANS DATA INTO 1 LINE PER MATCH
# Nested loop at end should give me 'picks_bans' data in a single line formatted as:
# "Match details", + 1is_pick, 1team, 1hero_id, 2is_pick,...
results=[]
with open('picks_bans/leagueid_10979_starladder_picks_bans.csv', 'a') as picks:
    for m in matches:
        #curmatch = data["match_id"][0]["picks_bans"].index(m) # !! Stuck @ this step 
        curmatch = data[['match_id','leagueid','series_id','series_type','duration', 'dire_team_id','radiant_team_id','radiant_win','picks_bans']]
        print(f" processsing match: {m['match_id']}")
        if 'picks_ban' in curmatch: 
            print( 'm' + str(match_id))
            picks.write(str(match_id) + ",") # match_id
            picks.write(str(dire_team_id) + ",") # team playing on dire side 
            picks.write(str(radiant_team_id) + ",") # team playin on radiant side
            picks.write(str(curmatch['radiant_win']) + ",") # match result 
            picks.write(str(curmatch['duration'])) # length of match 
            picklist = curmatch['picks_bans'] # define picks_bans feature as 'picklist'
            for i in range(len(picklist)):
                picks.write("," + str(picklist[i]['is_pick']) + "," + str(picklist[i]['team']) + "," + str(picklist[i]['hero_id'])) 
            picks.write("\n")
            




#########################################

# picks_ban parse of matchdata as dataframe


# ref: https://kite.com/python/answers/how-to-append-rows-to-a-pandas-dataframe-using-a-for-loop-in-python
#pandas.Dataframe.append(data, ignore_index=None)

# list of match_id's for the event

input_file = open('opendota_matches/match_list/league_id_10979_starladder_s2.json') 
matches = json.load(input_file) # !! list of match_id's for given event
input_file.close()

# JSON file with match data from get request
with open('opendota_matches/matches/league_id_10979_starladder_s2_matchdata.json', 'r') as matchdata:
    JSONcontent = json.load(matchdata) # matchdata now deserialized json object 
#matchdata.close()

data = json_normalize(JSONcontent) #json object --> table 


# GO THROUGH MATCH DATA AND EXTRACT PICKS_BANS FEATURE AND WRITE PICKS_BANS DATA INTO 1 LINE PER MATCH
# Nested loop at end should give me 'picks_bans' data in a single line formatted as:
# "Match details", + 1is_pick, 1team, 1hero_id, 2is_pick,...
results=[]
with open('picks_bans/leagueid_10979_starladder_picks_bans.csv', 'a') as picks:
    for m in matches:
        #curmatch = data["match_id"][0]["picks_bans"].index(m) # !! Stuck @ this step 
        curmatch = data[['match_id','leagueid','series_id','series_type','duration', 'dire_team_id','radiant_team_id','radiant_win','picks_bans']]
        print(f" processsing match: {m['match_id']}")
        #if 'picks_ban' in curmatch: 
        for i in range(order)
            print( 'm' + str(match_id))
            picks.write(str(match_id) + ",") # match_id
            picks.write(str(dire_team_id) + ",") # team playing on dire side 
            picks.write(str(radiant_team_id) + ",") # team playin on radiant side
            picks.write(str(curmatch['radiant_win']) + ",") # match result 
            picks.write(str(curmatch['duration'])) # length of match 
            picklist = curmatch['picks_bans'] # define picks_bans feature as 'picklist'
            for i in range(len(picklist)):
                picks.write("," + str(picklist[i]['is_pick']) + "," + str(picklist[i]['team']) + "," + str(picklist[i]['hero_id'])) 
            picks.write("\n")


