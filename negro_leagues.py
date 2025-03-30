import pandas as pd
import time

franchise = ['KCM','CAG','BBB','MRS','DS','SLS','CSW','ABC','CBN']
for year in range(1924,1949):
    try: 
        for team_name in franchise:
            try:
                overall_stats_df = pd.read_html(f'https://www.baseball-reference.com/teams/{team_name}/{year}.shtml')
                offensive_stats_df = overall_stats_df[0]
                time.sleep(20)  
                if 'KCM' in franchise:
                    offensive_stats_df.to_csv(f'negro_leagues/{year}_kansas_city_monarchs_offensive_stats.csv',index=False)
                if 'CAG' in franchise:
                    offensive_stats_df.to_csv(f'negro_leagues/{year}_chicago_american_giants_offensive_stats.csv',index=False)
            except Exception as e:
                print(f'offensive stats data for {team_name} does not exist for the {year} Season - {type(e)}')       
    except Exception as e:
        print(f'cannot filter rows accordingly - {type(e)}')    