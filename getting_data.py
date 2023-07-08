import os
import sys
import math
import pandas as pd
import requests
from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.endpoints import playercareerstats

# Get the NBA players from the API and create data-frames.
nba_players = players.get_players()
df = pd.DataFrame(nba_players)

# List of only active players -- 2 ways to do the same thing.
active_player_ids = df.loc[df['is_active'], 'id'].tolist()
active_players = players.get_active_players()

# This function gets the data of any player given the ID.
def get_player_data(nba_player_id):
    player_info = commonplayerinfo.CommonPlayerInfo(player_id=nba_player_id, timeout=100)
    df = player_info.common_player_info.get_data_frame()
    return df

# This is all to get the NBA API more efficently. Split and extract the data in fourths, rather than all at once (was taking to long).
player_career_data = []
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

for nba_player_id in fourth_1:
    career = playercareerstats.PlayerCareerStats(player_id = nba_player_id, timeout=100)
    temp = career.get_data_frames()[0]
    sliced = temp.iloc[:, [1] + list(range(3, temp.shape[1]))]
    player_career_data.append(sliced)
# End data extraction.

# Writing the data to a .txt file.
file_path = "data.txt"

with open(file_path, 'w') as file:
    for i, j in zip(range(0, 134), range(0, 134)):
        file.write(str(active_players[i]['full_name']) + '\n' + str((player_career_data[j])) + '\n')
# End writing --> .txt file.