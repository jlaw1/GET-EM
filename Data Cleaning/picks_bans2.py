# SOURCE: https://medium.com/@waprin/python-and-dota2-analyzing-team-liquids-io-success-and-failure-7d44cc5979b2

import json
import time
import requests

class Match:
    def __init__(self, match, radiant_win):
        self.match = match
        self.radiant_win= radiant_win
        self.radiant_picks = []
        self.radiant_bans = []
        self.dire_picks = []
        self.dire_bans = []

# # Matches hero_id to hero name
# names = {}
# with open('heroes.json') as f:
#     data = json.load(f)
#     for h in data:
#         names[h['id']] = h['localized_name']


def process_match(match):
    try:
        liquid_dire = match['dire_team']['team_id'] == 2163
    except:
        liquid_dire = match['dire_team_id'] == 2163

    if liquid_dire:
        liquid_win = not match['radiant_win']
    else:
        liquid_win = match['radiant_win']

    m = Match(match['match_id'], liquid_win)

    for pb in match['picks_bans']:
        if pb['team'] == liquid_dire and pb['is_pick']:
            m.liquid_picks.append(names[pb['hero_id']])
        if pb['team'] == liquid_dire and not pb['is_pick']:
            m.liquid_bans.append(names[pb['hero_id']])
        if pb['team'] != liquid_dire and pb['is_pick']:
            m.opponent_picks.append(names[pb['hero_id']])
        if pb['team'] != liquid_dire and not pb['is_pick']:
            m.opponent_bans.append(names[pb['hero_id']])
    return m


with open('liquid_match_data.txt') as f:
    matches = f.readlines()

processed = 0
errors = 0
processed_matches = []
for match in matches:
    match = json.loads(match)
    # Ignore matches before current roster
    if match['start_time'] < 1473984000:
        continue
    try:
        processed_matches.append(process_match(match))
        processed += 1
    except Exception as e:
        errors += 1
        #print("Error processing match error {}\n".format( e))

print("Processed {} Errors {}".format(processed, errors))