import pandas as pd


# 2/16/2025 - IN PROGRESS
df = pd.read_csv('mlb/2016_los_angeles_dodgers_offensive_stats.csv')

# df = df.loc[df['Player'] != 'Player']
df = df.sort_values(by=['RBI'], ascending=False)

df.to_csv('test.csv', index=False)

def filtering(x):
    return df[(df['Player'] != 'Player') | 
              (df['Player'] != '') | 
              (df['Player'] != 'Player') | 
              (df['Player'] != 'Player').sort_values(by=['RBI'], ascending=False)]

df = filtering(df)

print(df)

df.to_csv('test.csv', index=False)