import requests
import json
import pytz # Time Zone library
from datetime import datetime
from dotenv import load_dotenv
import os
import google.auth
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

load_dotenv()

api_key = os.getenv("API_KEY") # Got free API key from football data .org
LIVERPOOL_ID = 64 # Liverpools ID but can change to different team that suits
SCOPES = ['https://www.googleapis.com/auth/calendar']

def get_calendar_service():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    service = build('calendar', 'v3', credentials=creds)
    return service

def add_event_to_calendar(service, summary, description, start_time, end_time):
    event = {
        'summary': summary,
        'description': description,
        'start': {
            'dateTime': start_time.isoformat(),
            'timeZone': 'Australia/Sydney',
        },
        'end': {
            'dateTime': end_time.isoformat(),
            'timeZone': 'Australia/Sydney',
        },
    }
    event = service.events().insert(calendarId='primary', body=event).execute()
    print(f'Event created: {event.get("htmlLink")}')

def get_liverpool_fixtures():
    url = f'https://api.football-data.org/v4/teams/{LIVERPOOL_ID}/matches'
    headers = {'X-Auth-Token': api_key}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        fixtures = response.json()['matches']
        utc = pytz.utc
        sydney_tz = pytz.timezone('Australia/Sydney')

        service = get_calendar_service()  

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
                summary = f"{home_team} vs {away_team}"
                description = f"Competition: {comp_name}\nStatus: {status}"
                print(f"Upcoming match: {summary} on {match_date_aus.strftime('%Y-%m-%d %H:%M:%S')}")
                
                # Add event to Google Calendar
                start_time = match_date_aus
                end_time = match_date_aus.replace(hour=match_date_aus.hour + 2)
                add_event_to_calendar(service, summary, description, start_time, end_time)
    else:
        print(f"Error: {response.status_code}")

get_liverpool_fixtures()

