import pandas as pd


# 2/16/2025 - IN PROGRESS
los_angeles_dodgers_offensive_stats_df = pd.read_csv('mlb/2016_los_angeles_dodgers_offensive_stats.csv')

print('\nlos_angeles_dodgers_offensive_stats_df:\n',los_angeles_dodgers_offensive_stats_df)

def filtering(df):
    try: 
        return df[(df['Player'] != 'Player') & 
                (df['Player'] != 'Team Totals') & 
                (df['Player'] != 'Non-Pitcher Totals') & 
                (df['Player'] != 'Pitcher Totals')]
    except Exception as e:
        print('cannot filter rows of dataframe accordingly')

los_angeles_dodgers_offensive_stats_df = filtering(los_angeles_dodgers_offensive_stats_df)

los_angeles_dodgers_offensive_stats_df['RBI'] = los_angeles_dodgers_offensive_stats_df['RBI']

print('\nlos_angeles_dodgers_offensive_stats_df:\n',los_angeles_dodgers_offensive_stats_df)

los_angeles_dodgers_offensive_stats_df.to_csv('2016_los_angeles_dodgers_offensive_stats.csv', index=False)