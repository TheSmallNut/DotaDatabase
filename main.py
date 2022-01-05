import steam, requests, json
from secretKeys import STEAMAPIKEY
KEY = STEAMAPIKEY

#URL = f"https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?key={KEY}"

NEWURL = f"https://api.steampowered.com/IDOTA2Match_205790/GetMatchHistoryBySequenceNum/v1/?key={KEY}&start_at_match_seq_num="


r = requests.get(NEWURL).json()

i = 0

for match in r["result"]["matches"]:
    i += 1

print(i)



#with open('database.json', 'w') as outfile:
    #json.dump(r, outfile)