import pandas as pd
import time
import datetime

today = datetime.date.today()
current_year = today.strftime("%Y")
current_year = int(current_year) # 1 will be added to the value when the 2025 season begins

# mlb stats 2016-present (oakland athletics omitted due to moving out of oakland as of the 2025 season)
for x in range(2016,current_year):
    arizona_diamondbacks_stats_df = pd.read_html(f'https://www.baseball-reference.com/teams/ARI/{x}.shtml')
    arizona_diamondbacks_offensive_stats_df = arizona_diamondbacks_stats_df[0]
    arizona_diamondbacks_offensive_stats_df.to_csv(f'mlb/{x}_arizona_diamondbacks_offensive_stats.csv', index=False)    
    time.sleep(20)
    atlanta_braves_stats_df = pd.read_html(f'https://www.baseball-reference.com/teams/ATL/{x}.shtml')
    atlanta_braves_offensive_stats_df = atlanta_braves_stats_df[0]    
    atlanta_braves_offensive_stats_df.to_csv(f'mlb/{x}_atlanta_braves_offensive_stats.csv', index=False)    
    time.sleep(20)
    baltimore_orioles_stats_df = pd.read_html(f'https://www.baseball-reference.com/teams/BAL/{x}.shtml')
    baltimore_orioles_offensive_stats_df = baltimore_orioles_stats_df[0]
    baltimore_orioles_offensive_stats_df.to_csv(f'mlb/{x}_baltimore_orioles_offensive_stats.csv', index=False)    
    time.sleep(20)
    boston_red_sox_stats_df = pd.read_html(f'https://www.baseball-reference.com/teams/BOS/{x}.shtml')
    boston_red_sox_offensive_stats_df = boston_red_sox_stats_df[0]
    boston_red_sox_offensive_stats_df.to_csv(f'mlb/{x}_boston_red_sox_offensive_stats.csv', index=False)
    time.sleep(20)
    chicago_cubs_stats_df = pd.read_html(f'https://www.baseball-reference.com/teams/CHC/{x}.shtml')
    chicago_cubs_offensive_stats_df = chicago_cubs_stats_df[0]
    chicago_cubs_offensive_stats_df.to_csv(f'mlb/{x}_chicago_cubs_offensive_stats.csv', index=False)
    time.sleep(20)
    chicago_white_sox_stats_df = pd.read_html(f'https://www.baseball-reference.com/teams/CHW/{x}.shtml')
    chicago_white_sox_offensive_stats_df = chicago_white_sox_stats_df[0]
    chicago_white_sox_offensive_stats_df.to_csv(f'mlb/{x}_chicago_white_sox_offensive_stats.csv', index=False)
    time.sleep(20)
    cincinnati_reds_stats_df = pd.read_html(f'https://www.baseball-reference.com/teams/CIN/{x}.shtml')
    cincinnati_reds_offensive_stats_df = cincinnati_reds_stats_df[0]
    cincinnati_reds_offensive_stats_df.to_csv(f'mlb/{x}_cincinnati_reds_offensive_stats.csv', index=False)
    time.sleep(20)
    cleveland_guardians_stats_df = pd.read_html(f'https://www.baseball-reference.com/teams/CLE/{x}.shtml')
    cleveland_guardians_offensive_stats_df = cleveland_guardians_stats_df[0]
    cleveland_guardians_offensive_stats_df.to_csv(f'mlb/{x}_cleveland_guardians_offensive_stats.csv', index=False)
    time.sleep(20)
    colorado_rockies_stats_df = pd.read_html(f'https://www.baseball-reference.com/teams/COL/{x}.shtml')
    colorado_rockies_offensive_stats_df = colorado_rockies_stats_df[0]
    colorado_rockies_offensive_stats_df.to_csv(f'mlb/{x}_colorado_rockies_offensive_stats.csv', index=False)
    time.sleep(20)
    detroit_tigers_stats_df = pd.read_html(f'https://www.baseball-reference.com/teams/DET/{x}.shtml')
    detroit_tigers_offensive_stats_df = detroit_tigers_stats_df[0]
    detroit_tigers_offensive_stats_df.to_csv(f'mlb/{x}_detroit_tigers_offensive_stats.csv', index=False)
    time.sleep(20)
    houston_astros_stats_df = pd.read_html(f'https://www.baseball-reference.com/teams/HOU/{x}.shtml')
    houston_astros_offensive_stats_df = houston_astros_stats_df[0]
    houston_astros_offensive_stats_df.to_csv(f'mlb/{x}_houston_astros_offensive_stats.csv', index=False)
    time.sleep(20)
    kansas_city_royals_stats_df = pd.read_html(f'https://www.baseball-reference.com/teams/KCR/{x}.shtml')
    kansas_city_royals_offensive_stats_df = kansas_city_royals_stats_df[0]
    kansas_city_royals_offensive_stats_df.to_csv(f'mlb/{x}_kansas_city_royals_offensive_stats.csv', index=False)
    time.sleep(20)
    los_angeles_angels_stats_df = pd.read_html(f'https://www.baseball-reference.com/teams/LAA/{x}.shtml')
    los_angeles_angels_offensive_stats_df = los_angeles_angels_stats_df[0]
    los_angeles_angels_offensive_stats_df.to_csv(f'mlb/{x}_los_angeles_angels_offensive_stats.csv', index=False)
    time.sleep(20)
    los_angeles_dodgers_stats_df = pd.read_html(f'https://www.baseball-reference.com/teams/LAD/{x}.shtml')
    los_angeles_dodgers_offensive_stats_df = los_angeles_dodgers_stats_df[0]
    los_angeles_dodgers_offensive_stats_df.to_csv(f'mlb/{x}_los_angeles_dodgers_offensive_stats.csv', index=False)
    time.sleep(20)
    miami_marlins_stats_df = pd.read_html(f'https://www.baseball-reference.com/teams/MIA/{x}.shtml')
    miami_marlins_offensive_stats_df = miami_marlins_stats_df[0]
    miami_marlins_offensive_stats_df.to_csv(f'mlb/{x}_miami_marlins_offensive_stats.csv', index=False)
    time.sleep(20)
    milwaukee_brewers_stats_df = pd.read_html(f'https://www.baseball-reference.com/teams/MIL/{x}.shtml')
    milwaukee_brewers_offensive_stats_df = milwaukee_brewers_stats_df[0]
    milwaukee_brewers_offensive_stats_df.to_csv(f'mlb/{x}_milwaukee_brewers_offensive_stats.csv', index=False)
    time.sleep(20)
    minnesota_twins_stats_df = pd.read_html(f'https://www.baseball-reference.com/teams/MIN/{x}.shtml')
    minnesota_twins_offensive_stats_df = minnesota_twins_stats_df[0]
    minnesota_twins_offensive_stats_df.to_csv(f'mlb/{x}_minnesota_offensive_stats.csv', index=False)
    time.sleep(20)
    new_york_mets_stats_df = pd.read_html(f'https://www.baseball-reference.com/teams/NYM/{x}.shtml')
    new_york_mets_offensive_stats_df = new_york_mets_stats_df[0]
    new_york_mets_offensive_stats_df.to_csv(f'mlb/{x}_new_york_mets_offensive_stats.csv', index=False)
    time.sleep(20)
    new_york_yankees_stats_df = pd.read_html(f'https://www.baseball-reference.com/teams/NYY/{x}.shtml')
    new_york_yankees_offensive_stats_df = new_york_yankees_stats_df[0]
    new_york_yankees_offensive_stats_df.to_csv(f'mlb/{x}_new_york_yankees_offensive_stats.csv', index=False)
    time.sleep(20)    
    philadelphia_phillies_stats_df = pd.read_html(f'https://www.baseball-reference.com/teams/PHI/{x}.shtml')
    philadelphia_phillies_offensive_stats_df = philadelphia_phillies_stats_df[0]
    philadelphia_phillies_offensive_stats_df.to_csv(f'mlb/{x}_philadelphia_offensive_stats.csv', index=False)
    time.sleep(20)
    pittburgh_pirates_stats_df = pd.read_html(f'https://www.baseball-reference.com/teams/PIT/{x}.shtml')
    pittburgh_pirates_offensive_stats_df = pittburgh_pirates_stats_df[0]
    pittburgh_pirates_offensive_stats_df.to_csv(f'mlb/{x}_pittsburgh_pirates_offensive_stats.csv', index=False)
    time.sleep(20)
    san_diego_padres_stats_df = pd.read_html(f'https://www.baseball-reference.com/teams/SDP/{x}.shtml')
    san_diego_padres_offensive_stats_df = san_diego_padres_stats_df[0]
    san_diego_padres_offensive_stats_df.to_csv(f'mlb/{x}_san_diego_padres_offensive_stats.csv', index=False)
    time.sleep(20)
    san_francisco_giants_stats_df = pd.read_html(f'https://www.baseball-reference.com/teams/SFG/{x}.shtml')
    san_francisco_giants_offensive_stats_df = san_francisco_giants_stats_df[0]
    san_francisco_giants_offensive_stats_df.to_csv(f'mlb/{x}_san_francisco_giants_offensive_stats.csv', index=False)
    time.sleep(20)
    seattle_mariners_stats_df = pd.read_html(f'https://www.baseball-reference.com/teams/SEA/{x}.shtml')
    seattle_mariners_offensive_stats_df = seattle_mariners_stats_df[0]
    seattle_mariners_offensive_stats_df.to_csv(f'mlb/{x}_seattle_mariners_offensive_stats.csv', index=False)
    time.sleep(20)
    st_louis_cardinals_stats_df = pd.read_html(f'https://www.baseball-reference.com/teams/STL/{x}.shtml')
    st_louis_cardinals_offensive_stats_df = st_louis_cardinals_stats_df[0]
    st_louis_cardinals_offensive_stats_df.to_csv(f'mlb/{x}_st_louis_cardinals_offensive_stats.csv', index=False)
    time.sleep(20)
    tampa_bay_rays_stats_df = pd.read_html(f'https://www.baseball-reference.com/teams/TBR/{x}.shtml')
    tampa_bay_rays_offensive_stats_df = tampa_bay_rays_stats_df[0]
    tampa_bay_rays_offensive_stats_df.to_csv(f'mlb/{x}_tampa_bay_rays_offensive_stats.csv', index=False)
    time.sleep(20)
    texas_rangers_stats_df = pd.read_html(f'https://www.baseball-reference.com/teams/TEX/{x}.shtml')
    texas_rangers_offensive_stats_df = texas_rangers_stats_df[0]
    texas_rangers_offensive_stats_df.to_csv(f'mlb/{x}_texas_rangers_offensive_stats.csv', index=False)
    time.sleep(20)
    toronto_blue_jays_stats_df = pd.read_html(f'https://www.baseball-reference.com/teams/TOR/{x}.shtml')
    toronto_blue_jays_offensive_stats_df = toronto_blue_jays_stats_df[0]
    toronto_blue_jays_offensive_stats_df.to_csv(f'mlb/{x}_toronto_blue_jays_offensive_stats.csv', index=False)
    time.sleep(20)
    washington_nationals_stats_df = pd.read_html(f'https://www.baseball-reference.com/teams/WSN/{x}.shtml')
    washington_nationals_offensive_stats_df = washington_nationals_stats_df[0]
    washington_nationals_offensive_stats_df.to_csv(f'mlb/{x}_washington_nationals_offensive_stats.csv', index=False)
    time.sleep(20) # timing server requests accordingly to prevent 429 error

# oakland athletics 2016-2024 stats
for x in range(2016,2025):
    oakland_athletics_stats_df = pd.read_html(f'https://www.baseball-reference.com/teams/OAK/{x}.shtml')
    oakland_athletics_offensive_stats = oakland_athletics_stats_df[0]
    oakland_athletics_offensive_stats.to_csv(f'mlb/{x}_oakland_athletics_offensive_stats.csv', index=False)
    time.sleep(20) # timing server requests accordingly to prevent 429 error