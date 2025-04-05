import pandas as pd
import matplotlib.pyplot as plt

teams = ['kansas_city_monarchs','chicago_american_giants','birmingham_black_barons','memphis_red_sox','detroit_stars','st_louis_stars','cuban_stars_west','indianapolis_abcs','cleveland_browns']

for team in teams:
    try:
        for year in range(1924,1949):
            try:
                offensive_stats = pd.read_csv(f'negro_leagues/{year}_{team}_offensive_stats.csv')
                offensive_stats.to_csv(f'negro_leagues_cleanup/{year}_{team}_offensive_stats.csv')
            except Exception as e:
                print(f'cannot clean csv(s) - {type(e)}')
    except Exception as e:
        print(f'unable to find team(s) - {type(e)}')    