## TRYING TO PULL PRO DOTA MATCH DATA BY LEAGUE FROM OPEN DOTA 


import json
import pandas as pd
import requests
import numpy as np

# https://api.opendota.com/api/teams/{team_id}/matches

# Pro match api 

# https://api.opendota.com/api/proMatches
url = 'https://api.opendota.com/api/teams/{team_id}/matches'
{
  "match_id": 0,
  "duration": 0,
  "start_time": 0,
  "radiant_team_id": 0,
  "radiant_name": "string",
  "dire_team_id": 0,
  "dire_name": "string",
  "leagueid": 0,
  "league_name": "string",
  "series_id": 0,
  "series_type": 0,
  "radiant_score": 0,
  "dire_score": 0,
  "radiant_win": true,
  "radiant": true
}

JSONContent = requests.get(url).json()
content = json.dumps(JSONContent, indent = 4, sort_keys=True)
print(content)