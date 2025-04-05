import pandas as pd
import matplotlib.pyplot as plt

teams = ['KCM','CAG','BBB','MRS','DS','SLS','CSW','ABC','CBN']

for team in teams:
    for year in range(1924,1948):
        try:
            offensive_stats = pd.read_csv(f'https://www.baseball-reference.com/teams/{team}/{year}.csv')
        except Exception as e:
            print(f'cannot clean csv(s) - {type(e)}')