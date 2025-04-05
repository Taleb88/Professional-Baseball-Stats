import pandas as pd
import time

for year in range(1924,1949):
    try: 
        kansas_city_monarchs_overall_stats_df = pd.read_html(f'https://www.baseball-reference.com/teams/KCM/{year}.shtml')
        kansas_city_monarchs_offensive_stats_df = kansas_city_monarchs_overall_stats_df[0]
        kansas_city_monarchs_offensive_stats_df.to_csv(f'negro_leagues/{year}_kansas_city_monarchs_offensive_stats.csv',index=False)
        time.sleep(20) 
        chicago_american_giants_overall_stats_df = pd.read_html(f'https://www.baseball-reference.com/teams/CAG/{year}.shtml')
        chicago_american_giants_offensive_stats_df = chicago_american_giants_overall_stats_df[0]
        chicago_american_giants_offensive_stats_df.to_csv(f'negro_leagues/{year}_chicago_american_giants_offensive_stats.csv',index=False)
        time.sleep(20)
        birmingham_black_barons_overall_stats_df = pd.read_html(f'https://www.baseball-reference.com/teams/BBB/{year}.shtml')
        birmingham_black_barons_offensive_stats_df = birmingham_black_barons_overall_stats_df[0]
        birmingham_black_barons_offensive_stats_df.to_csv(f'negro_leagues/{year}_birmingham_black_barons_offensive_stats.csv',index=False)
        time.sleep(20)
        memphis_red_sox_overall_stats_df = pd.read_html(f'https://www.baseball-reference.com/teams/MRS/{year}.shtml')
        memphis_red_sox_offensive_stats_df = memphis_red_sox_overall_stats_df[0]
        memphis_red_sox_offensive_stats_df.to_csv(f'negro_leagues/{year}_memphis_red_sox_offensive_stats.csv',index=False)
        time.sleep(20)
        detroit_stars_overall_stats_df = pd.read_html(f'https://www.baseball-reference.com/teams/DS/{year}.shtml')
        detroit_stars_offensive_stats_df = detroit_stars_overall_stats_df[0]
        detroit_stars_offensive_stats_df.to_csv(f'negro_leagues/{year}_detroit_stars_offensive_stats.csv',index=False)
        time.sleep(20)
        st_louis_stars_overall_stats_df = pd.read_html(f'https://www.baseball-reference.com/teams/SLS/{year}.shtml')
        st_louis_stars_offensive_stats_df = st_louis_stars_overall_stats_df[0]
        st_louis_stars_offensive_stats_df.to_csv(f'negro_leagues/{year}_st_louis_stars_offensive_stats.csv',index=False)
        time.sleep(20)
        cuban_stars_west_overall_stats_df = pd.read_html(f'https://www.baseball-reference.com/teams/CSW/{year}.shtml')
        cuban_stars_west_offensive_stats_df = cuban_stars_west_overall_stats_df[0]
        cuban_stars_west_offensive_stats_df.to_csv(f'negro_leagues/{year}_cuban_stars_west_offensive_stats.csv',index=False)
        time.sleep(20)
        indianapolis_abcs_overall_stats_df = pd.read_html(f'https://www.baseball-reference.com/teams/ABC/{year}.shtml')
        indianapolis_abcs_offensive_stats_df = indianapolis_abcs_overall_stats_df[0]
        indianapolis_abcs_offensive_stats_df.to_csv(f'negro_leagues/{year}_indianapolis_abcs_offensive_stats.csv',index=False)
        time.sleep(20)
        cleveland_browns_overall_stats_df = pd.read_html(f'https://www.baseball-reference.com/teams/CBN/{year}.shtml')
        cleveland_browns_offensive_stats_df = cleveland_browns_overall_stats_df[0]
        cleveland_browns_offensive_stats_df.to_csv(f'negro_leagues/{year}_cleveland_browns_offensive_stats.csv',index=False)
        time.sleep(20)                                                             
    except Exception as e:
        print(f'data for certain seasons is not available at this time for certain teams - {type(e)}')    