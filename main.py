import steam, requests, json
from secretKeys import STEAMKEY
KEY = STEAMKEY

#URL = f"https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?key={KEY}"

NEWURL = f"https://api.steampowered.com/IDOTA2Match_205790/GetMatchHistoryBySequenceNum/v1/?key={KEY}&start_at_match_seq_num="


r = requests.get(NEWURL).json()
matches = r["result"]["matches"]
data = json.load(open('database.json'))


def playerExists(PlayerID):
    return True if str(PlayerID) in data["users"] else False




for match in matches:
    for player in match["players"]:
        playerID = player["account_id"]
        if not playerExists(playerID):
            data["users"][str(playerID)] = []



with open('database.json', 'w') as outfile:
    json.dump(data, outfile, indent = 4)