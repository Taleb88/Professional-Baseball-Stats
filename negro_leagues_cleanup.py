import pandas as pd
import matplotlib.pyplot as plt

teams = ['kansas_city_monarchs','chicago_american_giants','birmingham_black_barons','memphis_red_sox','detroit_stars','st_louis_stars','cuban_stars_west','indianapolis_abcs','cleveland_browns']

for team in teams:
    try:
        for year in range(1924,1949):
            try:
                offensive_stats_df = pd.read_csv(f'negro_leagues/{year}_{team}_offensive_stats.csv')
                # print(f'\n{year}_{team}_offensive_stats_df:\n',offensive_stats_df)
                # filtering out irrelevant values in Player column from all dataframes
                def hitter_column(df):
                    try: 
                        return df[(df['Player'] != 'Player') & 
                                (df['Player'] != 'Team Totals') & 
                                (df['Player'] != 'Non-Pitcher Totals') & 
                                (df['Player'] != 'Pitcher Totals')]
                    except Exception as e:
                        print(f'cannot filter rows of dataframe accordingly: {type(e)}')        
                offensive_stats_df = hitter_column(offensive_stats_df)
                offensive_stats_df[['RBI','PA','HR','SB']] = offensive_stats_df[['RBI','PA','HR','SB']].astype(int)
                offensive_stats_df = offensive_stats_df.sort_values(by=['RBI'], ascending=False).drop('Rk', axis=1)
                offensive_stats_df[['BA','OBP','SLG','OPS','rOBA']] = offensive_stats_df[['BA','OBP','SLG','OPS','rOBA']].astype(float).replace(0, 0.000)
                offensive_stats_df = offensive_stats_df.drop(['Pos.1','Awards'],axis=1)
                print(f'\n{year}_{team}_offensive_stats_df:\n',offensive_stats_df)
                offensive_stats_df.to_csv(f'negro_leagues_cleanup/{year}_{team}_offensive_stats.csv',index=False)
            except Exception as e:
                print(f'cannot certain clean csv(s) due to data not available for certain years/seasons - {type(e)}')
    except Exception as e:
        print(f'unable to find team(s) - {type(e)}')    