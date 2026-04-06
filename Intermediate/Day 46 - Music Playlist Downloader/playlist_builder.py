from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from song_data import search_list
from dotenv import load_dotenv
load_dotenv()
import os


CLIENT_SECRETS = os.getenv('CLIENT_SECRETS')
SCOPES = ['https://www.googleapis.com/auth/youtube']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
    
# Authorize the request and store authorization credentials.
def get_authenticated_service():
    creds = None
    # Load saved token if exists
    if os.path.exists("Intermediate/Day 46 - Music Playlist Downloader/token.json"):
        creds = Credentials.from_authorized_user_file("Intermediate/Day 46 - Music Playlist Downloader/token.json", SCOPES)
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS, SCOPES)
        creds = flow.run_local_server(
            port=0,
            access_type="offline",
            prompt="consent"
        )
        # Save token for reuse
        with open("Intermediate/Day 46 - Music Playlist Downloader/token.json", "w") as token:
            token.write(creds.to_json())

    return build(API_SERVICE_NAME, API_VERSION, credentials = creds)

def add_playlist(youtube):
  
    body = dict(
    snippet=dict(
        title="Your Weekly Mix 🎧",
        description="This is your weekly dose of top chartbusters in India."
    ),
    status=dict(
        privacyStatus='private'
    ) 
    ) 

    playlists_insert_response = youtube.playlists().insert(
    part='snippet,status',
    body=body
    ).execute()
    with open('Intermediate/Day 46 - Music Playlist Downloader/playlist_id.txt','w') as file:
        file.write(playlists_insert_response['id'])
        print('New playlist ID: %s' % playlists_insert_response['id'])

def add_song_to_playlist(youtube,playlist_id,list_of_songIDs):
    if list_of_songIDs:
        for id in list_of_songIDs:
            song_insert_response = youtube.playlistItems().insert(
                part="snippet",
                body={
                "snippet": {
                    "playlistId": playlist_id,
                    "position": 0,
                    "resourceId": {
                    "kind": "youtube#video",
                    "videoId": id
                    }
                }
                }
            ).execute()
            print(song_insert_response['snippet']['title'])
    else:
        print("No update to your Playlist.")

def search_songs(youtube,search_terms,list_of_playlist_videoIDs):
    search_result = []
    for term in search_terms:
        request = youtube.search().list(
            part="snippet",
            maxResults=1,
            q=term
        )
        response = request.execute()
        if response['items'][0]['id']['videoId'] not in list_of_playlist_videoIDs:
            search_result.append(response['items'][0]['id']['videoId'])
            print("Song ID not in playlist : ",response['items'][0]['id']['videoId'])
        else:
            print("Song ID already in playlist : ",response['items'][0]['id']['videoId'])
    return search_result

youtube = get_authenticated_service()

def get_playlist_items(youtube,playlist_id):
    list_of_playlist_videoIDs = []
    request = youtube.playlistItems().list(
        part="snippet,contentDetails",
        maxResults=10,
        playlistId=playlist_id
    )
    response = request.execute()
    for result in response['items']:
        list_of_playlist_videoIDs.append(result['contentDetails']['videoId'])
    return list_of_playlist_videoIDs

try:
    with open('Intermediate/Day 46 - Music Playlist Downloader/playlist_id.txt','r') as file:
        playlist_id = file.readline() #Read playlist ID stored in text file
        list_of_playlist_videoIDs = get_playlist_items(youtube,playlist_id) #get existing song IDs to compare
        list_of_songIDs = search_songs(youtube,search_list,list_of_playlist_videoIDs) #get list of songs to add
        add_song_to_playlist(youtube,playlist_id,list_of_songIDs) #finally add songs which are not in search_list
except FileNotFoundError as e:
    add_playlist(youtube)
except HttpError as e:
    print("Failed Request :",e.status_code)