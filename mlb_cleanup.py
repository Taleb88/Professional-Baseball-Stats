import pandas as pd
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
# # offensive stats
for x in range(2016,current_year):
    try: 
        for y in mlb_teams:
            offensive_stats_df = pd.read_csv(f'mlb/{x}_{y}_offensive_stats.csv')
            print(f'\n{x}_{y}_offensive_stats_df:\n',offensive_stats_df)
            # filtering out irrevalent values in Player column from all dataframes
            def player_column(df):
                try: 
                    return df[(df['Player'] != 'Player') & 
                              (df['Player'] != 'Team Totals') & 
                              (df['Player'] != 'Non-Pitcher Totals') & 
                              (df['Player'] != 'Pitcher Totals')]
                except Exception as e:
                    print(f'cannot filter rows of dataframe accordingly: {type(e)}')        

            offensive_stats_df = player_column(offensive_stats_df)
            offensive_stats_df['RBI'] = offensive_stats_df['RBI'].astype(int)
            offensive_stats_df = offensive_stats_df.sort_values(by=['RBI'], ascending=False).drop('Rk', axis=1).fillna(0)
            offensive_stats_df[['BA','OBP','SLG','OPS','rOBA']] = offensive_stats_df[['BA','OBP','SLG','OPS','rOBA']].astype(float).replace(0, 0.000)
            offensive_stats_df.to_csv(f'mlb_cleanup/{x}_{y}_offensive_stats.csv', index=False)
            print(f'\n{x}_{y}_offensive_stats_df:\n',offensive_stats_df)
    except Exception as e:
        print(f'unable to make proper updates: {type(e)}')
# oakland athletics only - offensive stats
for x in range(2016,2025):
    try: 
        offensive_stats_df = pd.read_csv(f'mlb/{x}_oakland_athletics_offensive_stats.csv')
        print(f'\n{x}_oakland_athletics_offensive_stats_df:\n',offensive_stats_df)
        # filtering out irrevalent values in Player column from all dataframes                
        def player_column(df):
            try: 
                return df[(df['Player'] != 'Player') & 
                          (df['Player'] != 'Team Totals') & 
                          (df['Player'] != 'Non-Pitcher Totals') & 
                          (df['Player'] != 'Pitcher Totals')]
            except Exception as e:
                print(f'cannot filter rows of dataframe accordingly: {type(e)}')        
       
        offensive_stats_df = player_column(offensive_stats_df)
        offensive_stats_df.to_csv(f'mlb_cleanup/{x}_oakland_athletics_offensive_stats.csv', index=False)
        offensive_stats_df['RBI'] = offensive_stats_df['RBI'].astype(int)
        offensive_stats_df = offensive_stats_df.sort_values(by=['RBI'], ascending=False).drop('Rk', axis=1).fillna(0)
        offensive_stats_df[['BA','OBP','SLG','OPS','rOBA']] = offensive_stats_df[['BA','OBP','SLG','OPS','rOBA']].astype(float).replace(0, 0.000)
        offensive_stats_df.to_csv(f'mlb_cleanup/{x}_oakland_athletics_offensive_stats.csv', index=False)
        print(f'\n{x}_oakland_athletics_offensive_stats_df:\n',offensive_stats_df)
    except Exception as e:
        print(f'unable to make proper updates: {type(e)}')
# pitching stats
for x in range(2016,current_year):
    try: 
        for y in mlb_teams:
            pitching_stats_df = pd.read_csv(f'mlb/{x}_{y}_pitching_stats.csv')
            print(f'\n{x}_{y}_pitching_stats_df:\n',pitching_stats_df)
            # filtering out irrevalent values in Player column from all dataframes
            def player_column(df):
                try: 
                    return df[(df['Player'] != 'Player') & 
                              (df['Player'] != 'Team Totals')]
                except Exception as e:
                    print(f'cannot filter rows of dataframe accordingly: {type(e)}')        

            pitching_stats_df = player_column(pitching_stats_df)
            pitching_stats_df.to_csv(f'mlb_cleanup/{x}_{y}_pitching_stats.csv', index=False)
            pitching_stats_df = pitching_stats_df.sort_values(by=['W'], ascending=False).drop('Rk', axis=1).fillna(0)
            pitching_stats_df[['W-L%','WHIP']] = pitching_stats_df[['W-L%','WHIP']].astype(float).replace(0, 0.000)    
            pitching_stats_df[['ERA','FIP','SO/BB']] = pitching_stats_df[['ERA','FIP','SO/BB']].astype(float).replace(0, 0.00)
            pitching_stats_df[['H9','HR9','BB9','SO9']] = pitching_stats_df[['H9','HR9','BB9','SO9']].astype(float).replace(0, 0.0) 
            pitching_stats_df['Player'] = pitching_stats_df['Player'].replace(0, 'RP')
            print(f'\n{x}_{y}_pitching_stats_df:\n',pitching_stats_df)
            pitching_stats_df.to_csv(f'mlb_cleanup/{x}_{y}_pitching_stats.csv', index=False)
    except Exception as e:
        print(f'unable to make proper updates: {type(e)}')
# oakland athletics only - pitching stats
for x in range(2016,2025):
    try: 
        pitching_stats_df = pd.read_csv(f'mlb/{x}_oakland_athletics_pitching_stats.csv')
        print(f'\n{x}_oakland_athletics_pitching_stats_df:\n',pitching_stats_df)
        # filtering out irrevalent values in Player column from all dataframes                
        def player_column(df):
            try: 
                return df[(df['Player'] != 'Player') & 
                          (df['Player'] != 'Team Totals')]
            except Exception as e:
                print(f'cannot filter rows of dataframe accordingly: {type(e)}')        
       
        pitching_stats_df = player_column(pitching_stats_df)
        pitching_stats_df.to_csv(f'mlb_cleanup/{x}_oakland_athletics_pitching_stats.csv', index=False)
        pitching_stats_df = pitching_stats_df.sort_values(by=['W'], ascending=False).drop('Rk', axis=1).fillna(0)
        pitching_stats_df[['W-L%','WHIP']] = pitching_stats_df[['W-L%','WHIP']].astype(float).replace(0, 0.000)    
        pitching_stats_df[['ERA','FIP','SO/BB']] = pitching_stats_df[['ERA','FIP','SO/BB']].astype(float).replace(0, 0.00)
        pitching_stats_df[['H9','HR9','BB9','SO9']] = pitching_stats_df[['H9','HR9','BB9','SO9']].astype(float).replace(0, 0.0) 
        pitching_stats_df['Player'] = pitching_stats_df['Player'].replace(0, 'RP')
        print(f'\n{x}_oakland_athletics_pitching_stats_df:\n',pitching_stats_df)      
        pitching_stats_df.to_csv(f'mlb_cleanup/{x}_oakland_athletics_pitching_stats.csv', index=False)  
    except Exception as e:
        print(f'unable to make proper updates: {type(e)}')  
