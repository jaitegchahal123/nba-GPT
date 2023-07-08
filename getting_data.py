import os
import sys
import math
import constants
import time
import pandas as pd
import requests
from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.endpoints import playercareerstats

nba_players = players.get_players()
df = pd.DataFrame(nba_players)


# List of only active players
active_player_ids = df.loc[df['is_active'], 'id'].tolist()


active_players = players.get_active_players()


#print(active_players[0]['full_name'])
#{'id': 1630173, 'full_name': 'Precious Achiuwa', 'first_name': 'Precious', 'last_name': 'Achiuwa', 'is_active': True}
#print(sliced_data)


# THIS GETS ALL PLAYER INFORMATION
def get_player_data(nba_player_id):
    player_info = commonplayerinfo.CommonPlayerInfo(player_id=nba_player_id, timeout=100)
    df = player_info.common_player_info.get_data_frame()
    return df


#all_player_data = []


player_career_data = []


#new
num_players = len(active_player_ids)
num_fourths = 4
players_per_fourth = math.ceil(num_players / num_fourths)


# Create four different arrays for each fourth of active players
fourths = [active_player_ids[i:i+players_per_fourth] for i in range(0, num_players, players_per_fourth)]


# Access each fourth array individually
fourth_1 = fourths[0]
fourth_2 = fourths[1]
fourth_3 = fourths[2]
fourth_4 = fourths[3]
#end


time.sleep(.600)

for nba_player_id in fourth_1:
# player_info = get_player_data(nba_player_id)
# all_player_data.append(player_info)
    career = playercareerstats.PlayerCareerStats(player_id = nba_player_id, timeout=100)
    temp = career.get_data_frames()[0]
    sliced = temp.iloc[:, [1] + list(range(3, temp.shape[1]))]

    player_career_data.append(sliced)


file_path = "data.txt"

print(len(active_players))
print(len(player_career_data))


# Write the player career data to the .txt file
time.sleep(.600)
with open(file_path, 'w') as file:
    for i, j in zip(range(0, 134), range(0, 134)):
# file.write(str(active_players[i]) + '\n')
# keys_to_exclude = ['id', 'full_name', 'first_name'] # Specify the keys to exclude


# sliced_data = [{key: player[key] for key in player.keys() if key not in keys_to_exclude} for player in active_players]
        file.write(str(active_players[i]['full_name']) + '\n' + str((player_career_data[j])) + '\n')
# file.write(data_final.to_string(index=False) + '\n')
# file.write(data_df.to_string(index=False) + '\n')


# career = playercareerstats.PlayerCareerStats(nbaPLAYER_id)
# df = career.get_data_frames()[0]