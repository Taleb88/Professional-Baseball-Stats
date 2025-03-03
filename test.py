# ALL CODE TESTED IN TEST.PY ONLY #


# import pandas as pd

# df = pd.read_csv('mlb_cleanup/2024_oakland_athletics_offensive_stats.csv')
# print(df)

# cols_list = list(df.columns)
# index = 0

# for col in cols_list:
#     print(index,col)
#     index += 1

# 3/2/2025 - IN PROGRESS - COMPLETE - SUCCESS
# import pandas as pd

# data = { 'name':['Taleb'] }

# df = pd.DataFrame(data)
# print(df)

# def bats(x):
#     if '#' in x:
#         return 'L'
#     else:
#         return 'R'

# df['bats'] = df.apply(lambda x: bats(x['name']), axis='columns')    

# print('updated:\n',df)


# # 2/28/2025 - IN PROGRESS - COMPLETE - WILL NOT BE USED; LOGIC IS CORRECT; ISSUES WITH WEBSITE WHEN PULLING DATA FROM TABLE(S)
# import pandas as pd

# minnesota_twins_stats_df = pd.read_html(f'https://www.baseball-reference.com/teams/MIN/2016.shtml')
# minnesota_twins_pitching_stats_df = minnesota_twins_stats_df[1]
# print(minnesota_twins_pitching_stats_df)


# # 2/22/2025 - IN PROGRESS - CHART CREATION - SUCCESS 
# import pandas as pd
# import matplotlib.pyplot as plt

# for year in range(2016,2021):
#     try:
#         offensive_stats_df = pd.read_csv(f'mlb/{year}_oakland_athletics_offensive_stats.csv')
#         color = 'green'
#         x = offensive_stats_df['Player']
#         y = offensive_stats_df['RBI']
#         plt.barh(x, y, color=color)
#         plt.title(f'Oakland Athletics RBI - {year} Season')
#         plt.yticks(fontsize=8)
#         plt.xlabel('Players')
#         plt.ylabel('RBIs')
#         plt.show()   
#     except Exception as e:
#         print(f'cannot create charts due to wrong year(s) - e - {type(e)}')


# 2/21/2025 - IN PROGRESS - CODE CLEANUP - CODE DOES NOT WORK; WILL NOT BE USED
# import pandas as pd
# import time
# import datetime

# today = datetime.date.today()
# current_year = today.strftime("%Y")
# current_year = int(current_year) # 1 will be added to the value when the 2025 season begins

# mlb_teams = ['arizona_diamondbacks','atlanta_braves']

# mlb_team_abbrev = ['ARI', 'ATL']
# # mlb stats 2023-present (oakland athletics omitted due to moving out of oakland as of the 2025 season)
# for x in range(2023,current_year):
#     try:
#         for y in mlb_team_abbrev:
#             mlb_team_stats = pd.read_html(f'https://www.baseball-reference.com/teams/{y}/{x}.shtml')
#             mlb_team_offensive_stats = mlb_team_stats[0]
#             for z in mlb_teams:
#                 mlb_team_offensive_stats.to_csv(f'mlb/{x}_{z}_offensive_stats.csv', index=False)    
#                 time.sleep(10) # timing server requests accordingly to prevent 429 error
#     except Exception as e:
#         print(f'cannot extract data from website:{type(e)}')


# 2/17/2025 - IN PROGRESS - DELETE UNNECESSARY FILES
# array = ['minnesota', 'philadelphia']
# for x in range(2016,2025):
#     for y in array:
#         if os.path.exists(f'mlb/{x}_{y}_offensive_stats.csv'):
#             os.remove(f'mlb/{x}_{y}_offensive_stats.csv')
#         else:
#             print('the files do not exist in the mlb folder')
        

# 2/16/2025 - SUCCESS - TO BE USED
# team = ['arizona_diamondbacks','atlanta_braves','baltimore_orioles',
#         'boston_red_sox','chicago_cubs','chicago_white_sox',
#         'cincinnati_reds','cleveland_guardians','colorado_rockies',
#         'detroit_tigers','houston_astros','kansas_city_royals',
#         'los_angeles_angels','los_angeles_dodgers','miami_marlins',
#         'milwaukee_brewers','minnesota_twins','new_york_mets',
#         'new_york_yankees','philadelphia_phillies','pittsburgh_pirates',
#         'san_diego_padres','san_francisco_giants','seattle_mariners',
#         'st_louis_cardinals','tampa_bay_rays','texas_rangers','toronto_blue_jays',
#         'washington_nationals']
# for x in range(2016,current_year):
#     try: 
#         for y in team:
#             offensive_stats_df = pd.read_csv(f'mlb/{x}_{y}_offensive_stats.csv')
#             print(f'\n{x}_{y}_offensive_stats_df:\n',offensive_stats_df)
            
#             def player_column(df):
#                 try: 
#                     return df[(df['Player'] != 'Player') & 
#                             (df['Player'] != 'Team Totals') & 
#                             (df['Player'] != 'Non-Pitcher Totals') & 
#                             (df['Player'] != 'Pitcher Totals')]
#                 except Exception as e:
#                     print('cannot filter rows of dataframe accordingly')

#             offensive_stats_df = player_column(offensive_stats_df)
#             offensive_stats_df['RBI'] = offensive_stats_df['RBI'].astype(int)
#             offensive_stats_df = offensive_stats_df.sort_values(by=['RBI'], ascending=False).drop('Rk', axis=1).fillna(0)
#             offensive_stats_df[['BA','OBP','SLG','OPS','rOBA']] = offensive_stats_df[['BA','OBP','SLG','OPS','rOBA']].astype(float).replace(0, 0.000)
#             offensive_stats_df.to_csv(f'csv/{x}_{y}_offensive_stats.csv', index=False)

#             print(f'\n{x}_{y}_offensive_stats_df:\n',offensive_stats_df)
#     except Exception as e:
#         print(f'unable to make proper updates: {type(e)}')

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