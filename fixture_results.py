import requests
import json
import pytz # Time Zone library
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY") # Got free API key from football data .org
LIVERPOOL_ID = 64 # Liverpools ID but can change to different team that suits

def get_liverpool_fixtures():
    url = f'https://api.football-data.org/v4/teams/{LIVERPOOL_ID}/matches'
    headers = {'X-Auth-Token': api_key}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        fixtures = response.json()['matches']
        utc = pytz.utc
        sydney_tz = pytz.timezone('Australia/Sydney')

        for match in fixtures:
            comp_name = match['competition']['name']
            home_team = match['homeTeam']['name']
            away_team = match['awayTeam']['name']

            match_date = datetime.strptime(match['utcDate'], "%Y-%m-%dT%H:%M:%SZ")
            match_date = utc.localize(match_date)

            match_date_aus = match_date.astimezone(sydney_tz) # Converting to Sydney TimeZone

            status = match['status']
            if status == 'FINISHED':
                match_result = match['score']['fullTime']
                print(f"Competition: {comp_name}")
                print(f"Match: {home_team} {match_result['home']} - {match_result['away']} {away_team}")
                print(f"Date (AUS / SYD): {match_date_aus.strftime('%Y-%m-%d %H:%M:%S')}")
                print('Fixture Complete\n')
            else:
                print(f"Competition: {comp_name}")
                print(f"Match: {home_team} vs {away_team}")
                print(f"Date / Time (AUS / SYD): {match_date_aus.strftime('%Y-%m-%d %H:%M:%S')}")
                print('Upcoming fixture\n')
    else:
        print(f"Error: {response.status_code}")

get_liverpool_fixtures()

