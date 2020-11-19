from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    return service


def get_today_events():
    service = main()
    now = datetime.datetime.utcnow().isoformat() + "-05:00"
    tomorrow_date = str((datetime.date.today() + datetime.timedelta(days=1)))
    tomorrow_iso = tomorrow_date+"T"+"00:00:00-05:00"
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        timeMax=tomorrow_iso, maxResults=100, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])

def get_tomorrow_events():
    service = main()
    tomorrow_start_date = str((datetime.date.today() + datetime.timedelta(days=1)))
    tomorrow_end_date = str(datetime.date.today() + datetime.timedelta(days=2))
    tomorrow_start_iso = tomorrow_start_date+"T"+"00:00:00-05:00"
    tomorrow_end_iso = tomorrow_end_date+"T"+"00:00:00-05:00"
    events_result = service.events().list(calendarId='primary', timeMin=tomorrow_start_iso,
                                        timeMax=tomorrow_end_iso, maxResults=100, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])

