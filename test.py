import pandas as pd


# 2/16/2025 - SUCCESS - TO BE USED
team = ['new_york_yankees', 'atlanta_braves']
for x in range(2016,2020):
    try: 
        for y in team:
            offensive_stats_df = pd.read_csv(f'mlb/{x}_{y}_offensive_stats.csv')
            print(f'\n{x}_{y}_offensive_stats_df:\n',offensive_stats_df)
            
            def player_column(df):
                try: 
                    return df[(df['Player'] != 'Player') & 
                            (df['Player'] != 'Team Totals') & 
                            (df['Player'] != 'Non-Pitcher Totals') & 
                            (df['Player'] != 'Pitcher Totals')]
                except Exception as e:
                    print('cannot filter rows of dataframe accordingly')

            offensive_stats_df = player_column(offensive_stats_df)
            offensive_stats_df['RBI'] = offensive_stats_df['RBI'].astype(int)
            offensive_stats_df = offensive_stats_df.sort_values(by=['RBI'], ascending=False).drop('Rk', axis=1).fillna(0)
            offensive_stats_df[['BA','OBP','SLG','OPS','rOBA']] = offensive_stats_df[['BA','OBP','SLG','OPS','rOBA']].astype(float).replace(0, 0.000)
            offensive_stats_df.to_csv(f'csv/{x}_{y}_offensive_stats.csv', index=False)

            print(f'\n{x}_{y}_offensive_stats_df:\n',offensive_stats_df)
    except Exception as e:
        print(f'unable to make proper updates: {type(e)}')

# 2/16/2025 - SUCCESS
# for x in range(2016,2019):
#     new_york_yankees_offensive_stats_df = pd.read_csv(f'mlb/{x}_new_york_yankees_offensive_stats.csv')
#     print('\nnew_york_yankees_offensive_stats_df:\n',new_york_yankees_offensive_stats_df)
    
#     def player_column(df):
#         try: 
#             return df[(df['Player'] != 'Player') & 
#                     (df['Player'] != 'Team Totals') & 
#                     (df['Player'] != 'Non-Pitcher Totals') & 
#                     (df['Player'] != 'Pitcher Totals')]
#         except Exception as e:
#             print('cannot filter rows of dataframe accordingly')

#     new_york_yankees_offensive_stats_df = player_column(new_york_yankees_offensive_stats_df)
#     new_york_yankees_offensive_stats_df['RBI'] = new_york_yankees_offensive_stats_df['RBI'].astype(int)
#     new_york_yankees_offensive_stats_df = new_york_yankees_offensive_stats_df.sort_values(by=['RBI'], ascending=False)
#     new_york_yankees_offensive_stats_df = new_york_yankees_offensive_stats_df.drop('Rk', axis=1)
#     new_york_yankees_offensive_stats_df.to_csv(f'csv/{x}_new_york_yankees_offensive_stats.csv', index=False)

#     print(f'\n{x}_new_york_yankees_offensive_stats_df:\n',new_york_yankees_offensive_stats_df)



# 2/16/2025 - IN PROGRESS - SUCCESS
# new_york_yankees_offensive_stats_df = pd.read_csv('mlb/2016_new_york_yankees_offensive_stats.csv')

# print('\nnew_york_yankees_offensive_stats_df:\n',new_york_yankees_offensive_stats_df)

# def filtering(df):
#     try: 
#         return df[(df['Player'] != 'Player') & 
#                 (df['Player'] != 'Team Totals') & 
#                 (df['Player'] != 'Non-Pitcher Totals') & 
#                 (df['Player'] != 'Pitcher Totals')]
#     except Exception as e:
#         print('cannot filter rows of dataframe accordingly')

# new_york_yankees_offensive_stats_df = filtering(new_york_yankees_offensive_stats_df)

# new_york_yankees_offensive_stats_df['RBI'] = new_york_yankees_offensive_stats_df['RBI'].astype(int)
# new_york_yankees_offensive_stats_df.to_csv('2016_new_york_yankees_offensive_stats.csv', index=False)

# print('\nnew_york_yankees_offensive_stats_df:\n',new_york_yankees_offensive_stats_df)

# new_york_yankees_offensive_stats_df = new_york_yankees_offensive_stats_df.sort_values(by=['RBI'],ascending=False)

# print('\nnew_york_yankees_offensive_stats_df:\n',new_york_yankees_offensive_stats_df)
# new_york_yankees_offensive_stats_df.to_csv('2016_new_york_yankees_offensive_stats.csv', index=False)