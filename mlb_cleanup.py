import pandas as pd
import matplotlib.pyplot as plt
import datetime

today = datetime.date.today()
current_year = today.strftime("%Y")
current_year = int(current_year) # 1 will be added to the value when the 2025 season begins

# data cleanup per team per year (2016-present)
mlb_teams = ['arizona_diamondbacks','atlanta_braves','baltimore_orioles',
        'boston_red_sox','chicago_cubs','chicago_white_sox',
        'cincinnati_reds','cleveland_guardians','colorado_rockies',
        'detroit_tigers','houston_astros','kansas_city_royals',
        'los_angeles_angels','los_angeles_dodgers','miami_marlins',
        'milwaukee_brewers','minnesota_twins','new_york_mets',
        'new_york_yankees','philadelphia_phillies','pittsburgh_pirates',
        'san_diego_padres','san_francisco_giants','seattle_mariners',
        'st_louis_cardinals','tampa_bay_rays','texas_rangers','toronto_blue_jays',
        'washington_nationals']
# offensive stats
for year in range(2016,current_year):
    try: 
        for mlb_team in mlb_teams:
            offensive_stats_df = pd.read_csv(f'mlb/{year}_{mlb_team}_offensive_stats.csv')
            # print(f'\n{x}_{y}_offensive_stats_df:\n',offensive_stats_df)
            # filtering out irrevalent values in Player column from all dataframes
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
            offensive_stats_df = offensive_stats_df.sort_values(by=['RBI'], ascending=False).drop('Rk', axis=1).fillna(0)
            offensive_stats_df[['BA','OBP','SLG','OPS','rOBA']] = offensive_stats_df[['BA','OBP','SLG','OPS','rOBA']].astype(float).replace(0, 0.000)
            offensive_stats_df.to_csv(f'mlb_cleanup/{year}_{mlb_team}_offensive_stats.csv', index=False)
            # adding new Bats column in all dataframes
            def bats(x):
                if '*' in x:
                    return 'Left'
                elif '#' in x:
                    return 'Both'
                else:
                    return 'Right'
            offensive_stats_df['Bats'] = offensive_stats_df.apply(lambda x: bats(x['Player']),axis='columns')
            # print(f'\n{year}_{mlb_team}_offensive_stats_df:\n',offensive_stats_df)
            offensive_stats_df.to_csv(f'mlb_cleanup/{year}_{mlb_team}_offensive_stats.csv', index=False)
            # confirming whether BA is under Mendoza Line in new 'Under Mendoza Line?' column based on criteria
            offensive_stats_df['Under Mendoza Line?'] = len(offensive_stats_df) * ['No']
            offensive_stats_df.loc[(offensive_stats_df['BA'] < 0.200) & (offensive_stats_df['PA'] >= 502), 'Under Mendoza Line?'] = 'Yes'
            offensive_stats_df.to_csv(f'mlb_cleanup/{year}_{mlb_team}_offensive_stats.csv', index=False)
            # 20/20, 30/30, 40/40, 50/50, 60/60, 20/70, 30/70, and 40/70 clubs based off on HR and SB in same season - new columns
            offensive_stats_df['20/20 Club'] = len(offensive_stats_df) * ['No']
            offensive_stats_df['30/30 Club'] = len(offensive_stats_df) * ['No'] 
            offensive_stats_df['40/40 Club'] = len(offensive_stats_df) * ['No'] 
            offensive_stats_df['50/50 Club'] = len(offensive_stats_df) * ['No']
            offensive_stats_df['60/60 Club'] = len(offensive_stats_df) * ['No']
            offensive_stats_df['20/70 Club'] = len(offensive_stats_df) * ['No']
            offensive_stats_df['30/70 Club'] = len(offensive_stats_df) * ['No']
            offensive_stats_df['40/70 Club'] = len(offensive_stats_df) * ['No']
            offensive_stats_df.loc[(offensive_stats_df['HR'] >= 20) & (offensive_stats_df['SB'] >= 20), '20/20 Club'] = 'Yes'
            offensive_stats_df.loc[(offensive_stats_df['HR'] >= 30) & (offensive_stats_df['SB'] >= 30), '30/30 Club'] = 'Yes'
            offensive_stats_df.loc[(offensive_stats_df['HR'] >= 40) & (offensive_stats_df['SB'] >= 40), '40/40 Club'] = 'Yes'
            offensive_stats_df.loc[(offensive_stats_df['HR'] >= 50) & (offensive_stats_df['SB'] >= 50), '50/50 Club'] = 'Yes'        
            offensive_stats_df.loc[(offensive_stats_df['HR'] >= 60) & (offensive_stats_df['SB'] >= 60), '60/60 Club'] = 'Yes'
            offensive_stats_df.loc[(offensive_stats_df['HR'] >= 20) & (offensive_stats_df['SB'] >= 70), '20/70 Club'] = 'Yes'
            offensive_stats_df.loc[(offensive_stats_df['HR'] >= 30) & (offensive_stats_df['SB'] >= 70), '30/70 Club'] = 'Yes'
            offensive_stats_df.loc[(offensive_stats_df['HR'] >= 40) & (offensive_stats_df['SB'] >= 70), '40/70 Club'] = 'Yes'                      
            print(f'\n{year}_{mlb_team}_offensive_stats_df:\n',offensive_stats_df)
            offensive_stats_df.to_csv(f'mlb_cleanup/{year}_{mlb_team}_offensive_stats.csv', index=False)               
    except Exception as e:
        print(f'unable to make proper updates: {type(e)}')
# oakland athletics only - offensive stats
for year in range(2016,2025):
    try: 
        offensive_stats_df = pd.read_csv(f'mlb/{year}_oakland_athletics_offensive_stats.csv')
        # print(f'\n{year}_oakland_athletics_offensive_stats_df:\n',offensive_stats_df)
        # filtering out irrevalent values in Player column from all dataframes                
        def oakland_athletics_hitter_column(df):
            try: 
                return df[(df['Player'] != 'Player') & 
                          (df['Player'] != 'Team Totals') & 
                          (df['Player'] != 'Non-Pitcher Totals') & 
                          (df['Player'] != 'Pitcher Totals')]
            except Exception as e:
                print(f'cannot filter rows of dataframe accordingly: {type(e)}')               
        offensive_stats_df = oakland_athletics_hitter_column(offensive_stats_df)
        offensive_stats_df.to_csv(f'mlb_cleanup/{year}_oakland_athletics_offensive_stats.csv', index=False)
        offensive_stats_df[['RBI','PA','HR','SB']] = offensive_stats_df[['RBI','PA','HR','SB']].astype(int)
        offensive_stats_df = offensive_stats_df.sort_values(by=['RBI'], ascending=False).drop('Rk', axis=1).fillna(0)
        offensive_stats_df[['BA','OBP','SLG','OPS','rOBA']] = offensive_stats_df[['BA','OBP','SLG','OPS','rOBA']].astype(float).replace(0, 0.000)
        offensive_stats_df.to_csv(f'mlb_cleanup/{year}_oakland_athletics_offensive_stats.csv', index=False)                
        print(f'\n{year}_oakland_athletics_offensive_stats_df:\n',offensive_stats_df)
        # adding new Bats column in all dataframes
        def bats(x):
            if '*' in x:
                return 'Left'
            elif '#' in x:
                return 'Both'
            else:
                return 'Right'
        offensive_stats_df['Bats'] = offensive_stats_df.apply(lambda x: bats(x['Player']),axis='columns')
        # print(f'\n{year}_oakland_athletics_offensive_stats_df:\n',offensive_stats_df)
        offensive_stats_df.to_csv(f'mlb_cleanup/{year}_oakland_athletics_offensive_stats.csv', index=False)
        # confirming whether BA is under Mendoza Line in new 'Under Mendoza Line?' column
        offensive_stats_df['Under Mendoza Line?'] = len(offensive_stats_df) * ['No']
        offensive_stats_df.loc[(offensive_stats_df['BA'] < 0.200) & (offensive_stats_df['PA'] >= 502), 'Under Mendoza Line?'] = 'Yes'
        offensive_stats_df.to_csv(f'mlb_cleanup/{year}_oakland_athletics_offensive_stats.csv', index=False)
        # 20/20, 30/30, 40/40, 50/50, 60/60, 20/70, 30/70, and 40/70 clubs based off on HR and SB in same season - new columns
        offensive_stats_df['20/20 Club'] = len(offensive_stats_df) * ['No']
        offensive_stats_df['30/30 Club'] = len(offensive_stats_df) * ['No'] 
        offensive_stats_df['40/40 Club'] = len(offensive_stats_df) * ['No'] 
        offensive_stats_df['50/50 Club'] = len(offensive_stats_df) * ['No']
        offensive_stats_df['60/60 Club'] = len(offensive_stats_df) * ['No']
        offensive_stats_df['20/70 Club'] = len(offensive_stats_df) * ['No']
        offensive_stats_df['30/70 Club'] = len(offensive_stats_df) * ['No']
        offensive_stats_df['40/70 Club'] = len(offensive_stats_df) * ['No']        
        offensive_stats_df.loc[(offensive_stats_df['HR'] >= 20) & (offensive_stats_df['SB'] >= 20), '20/20 Club'] = 'Yes'
        offensive_stats_df.loc[(offensive_stats_df['HR'] >= 30) & (offensive_stats_df['SB'] >= 30), '30/30 Club'] = 'Yes'
        offensive_stats_df.loc[(offensive_stats_df['HR'] >= 40) & (offensive_stats_df['SB'] >= 40), '40/40 Club'] = 'Yes'
        offensive_stats_df.loc[(offensive_stats_df['HR'] >= 50) & (offensive_stats_df['SB'] >= 50), '50/50 Club'] = 'Yes'        
        offensive_stats_df.loc[(offensive_stats_df['HR'] >= 60) & (offensive_stats_df['SB'] >= 60), '60/60 Club'] = 'Yes'
        offensive_stats_df.loc[(offensive_stats_df['HR'] >= 20) & (offensive_stats_df['SB'] >= 70), '20/70 Club'] = 'Yes'
        offensive_stats_df.loc[(offensive_stats_df['HR'] >= 30) & (offensive_stats_df['SB'] >= 70), '30/70 Club'] = 'Yes'
        offensive_stats_df.loc[(offensive_stats_df['HR'] >= 40) & (offensive_stats_df['SB'] >= 70), '40/70 Club'] = 'Yes'                      
        print(f'\n{year}_oakland_athletics_offensive_stats_df:\n',offensive_stats_df)
        offensive_stats_df.to_csv(f'mlb_cleanup/{year}_oakland_athletics_offensive_stats.csv', index=False)
        # players with at least 100 RBIs
        players_with_at_least_100_rbis = offensive_stats_df.loc[offensive_stats_df['RBI'] >= 100]
        print(f'\n{year}_oakland_athletics_players_with_at_least_100_rbis_df:\n',players_with_at_least_100_rbis)
        # visualizations
        offensive_stats_df = pd.read_csv(f'mlb_cleanup/{year}_oakland_athletics_offensive_stats.csv')
        color = 'green'
        x = offensive_stats_df['Player']
        y = offensive_stats_df['RBI']
        plt.barh(x, y, color=color)
        plt.title(f'Oakland Athletics RBI - {year} Season')
        plt.yticks(fontsize=9)
        plt.xlabel('RBIs')
        plt.ylabel('Players')
        plt.gca().invert_yaxis() # displaying highest RBI value first       
        plt.show()   
    except Exception as e:
        print(f'unable to make proper updates: {type(e)}')


# # pitching stats - WILL NOT BE IN PROJECT FOR NOW
# for x in range(2016,current_year):
#     try:
#         for y in mlb_teams:
#             pitching_stats_df = pd.read_csv(f'mlb/{x}_{y}_pitching_stats.csv')
#             print(f'\n{x}_{y}_pitching_stats_df:\n',pitching_stats_df)
#             #filtering out irrevalent values in Player column from all dataframes
#             def player_column(df):
#                 try: 
#                     return df[(df['Player'] != 'Player') & 
#                               (df['Player'] != 'Team Totals')]
#                 except Exception as e:
#                     print(f'cannot filter rows of dataframe accordingly: {type(e)}')        

#             pitching_stats_df = player_column(pitching_stats_df)
#             print(f'\n{x}_{y}_pitching_stats_df:\n',pitching_stats_df)
#             pitching_stats_df.to_csv(f'mlb_cleanup/{x}_{y}_pitching_stats.csv', index=False)
#             pitching_stats_df = pitching_stats_df.sort_values(by=['W'], ascending=False).drop('Rk', axis=1).fillna(0)
#             pitching_stats_df[['W-L%','WHIP']] = pitching_stats_df[['W-L%','WHIP']].astype(float).replace(0, 0.000)    
#             pitching_stats_df[['ERA','FIP','SO/BB']] = pitching_stats_df[['ERA','FIP','SO/BB']].astype(float).replace(0, 0.00)
#             pitching_stats_df[['H9','HR9','BB9','SO9']] = pitching_stats_df[['H9','HR9','BB9','SO9']].astype(float).replace(0, 0.0) 
#             pitching_stats_df['Player'] = pitching_stats_df['Player'].replace(0, 'RP')
#             print(f'\n{x}_{y}_pitching_stats_df:\n',pitching_stats_df)
#             pitching_stats_df.to_csv(f'mlb_cleanup/{x}_{y}_pitching_stats.csv', index=False)
#     except Exception as e:
#         print(f'unable to make proper updates: {type(e)}')
# # oakland athletics only - pitching stats
# for x in range(2016,2025):
#     try: 
#         pitching_stats_df = pd.read_csv(f'mlb/{x}_oakland_athletics_pitching_stats.csv')
#         print(f'\n{x}_oakland_athletics_pitching_stats_df:\n',pitching_stats_df)
#         # filtering out irrevalent values in Player column from all dataframes                
#         def player_column(df):
#             try: 
#                 return df[(df['Player'] != 'Player') & 
#                           (df['Player'] != 'Team Totals')]
#             except Exception as e:
#                 print(f'cannot filter rows of dataframe accordingly: {type(e)}')        
       
#         pitching_stats_df = player_column(pitching_stats_df)
#         print(f'\n{x}_oakland_athletics_pitching_stats_df:\n',pitching_stats_df)
#         pitching_stats_df.to_csv(f'mlb_cleanup/{x}_oakland_athletics_pitching_stats.csv', index=False)
#         pitching_stats_df = pitching_stats_df.sort_values(by=['W'], ascending=False).drop('Rk', axis=1).fillna(0)
#         pitching_stats_df[['W-L%','WHIP']] = pitching_stats_df[['W-L%','WHIP']].astype(float).replace(0, 0.000)    
#         pitching_stats_df[['ERA','FIP','SO/BB']] = pitching_stats_df[['ERA','FIP','SO/BB']].astype(float).replace(0, 0.00)
#         pitching_stats_df[['H9','HR9','BB9','SO9']] = pitching_stats_df[['H9','HR9','BB9','SO9']].astype(float).replace(0, 0.0) 
#         pitching_stats_df['Player'] = pitching_stats_df['Player'].replace(0, 'RP')
#         print(f'\n{x}_oakland_athletics_pitching_stats_df:\n',pitching_stats_df)      
#         pitching_stats_df.to_csv(f'mlb_cleanup/{x}_oakland_athletics_pitching_stats.csv', index=False)  
#     except Exception as e:
#         print(f'unable to make proper updates: {type(e)}')  