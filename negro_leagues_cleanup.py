import pandas as pd

teams = [] # abbrevations per team to be filled in

for team in teams:
    for year in range(1924,1948):
        offensive_stats = pd.read_csv(f'https://www.baseball-reference.com/teams/{team}/{year}.shtml')