import pandas as pd
import time

# kansas city monarchs - 1924-1930 and 1937-1948 seasons only available via baseball-reference.com
for year in range(1924,1949):
    try: 
        kansas_city_monarchs_stats_df = pd.read_html(f'https://www.baseball-reference.com/teams/KCM/{year}.shtml')
        kansas_city_monarchs_offensive_stats_df = kansas_city_monarchs_stats_df[0]
        kansas_city_monarchs_offensive_stats_df.to_csv(f'negro_leagues/{year}_kansas_city_monarchs_offensive_stats.csv')
        time.sleep(20)    
    except Exception as e:
        print(f'offensive stats data does not exist for the {year} Season - {type(e)}')    