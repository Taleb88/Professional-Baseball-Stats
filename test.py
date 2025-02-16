import pandas as pd


# 2/16/2025 - IN PROGRESS
df = pd.read_csv('mlb/2016_los_angeles_dodgers_offensive_stats.csv')
print(df.sort_values(by=['RBI'], ascending=False))