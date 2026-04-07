from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from song_data import search_list
from dotenv import load_dotenv
load_dotenv()
import os
from datetime import datetime

CLIENT_SECRETS_FILE = './Intermediate/Day 46 - Music Playlist Downloader/client_secrets_file.json'
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
        flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
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
    response = youtube.playlists().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": f"Your Weekly Mix 🎧",
                "description": f"This is your weekly dose of top chartbusters 🔥 - {datetime.now().strftime('%d %b %Y')}."
            },
            "status": {
                "privacyStatus": "private"
            }
        }
        ).execute()
    with open('Intermediate/Day 46 - Music Playlist Downloader/playlist_id.txt','w') as file:
        file.write(response['id'])
        print('New playlist ID: %s' % response['id'])

def add_song_to_playlist(youtube,playlist_id,list_of_new_songIDs):
    if list_of_new_songIDs:
        for id in list_of_new_songIDs:
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

def delete_song_from_playlist(youtube,list_of_new_songIDs,list_of_playlist_itemID):
    for item_id in list_of_playlist_itemID[:len(list_of_new_songIDs)]:
        try:
            youtube.playlistItems().delete(id = item_id).execute()
            print('Deleted Song ID : ',item_id)
        except Exception as e:
            print("Something went wrong! ",e)

def search_songs(youtube,search_terms,list_of_playlist_videoID):
    search_result = []
    
    for term in search_terms:
        request = youtube.search().list(
            part="snippet",
            maxResults=1,
            q=term
        )
        response = request.execute()
        if response['items'][0]['id']['videoId'] not in list_of_playlist_videoID:
            search_result.append(response['items'][0]['id']['videoId'])
            print("Song ID not in playlist : ",response['items'][0]['id']['videoId'])
        else:
            print("Song ID already in playlist : ",response['items'][0]['id']['videoId'])
    return search_result



def get_playlist_items(youtube,playlist_id):
    list_of_playlist_videoIDs_itemIDs = []
    request = youtube.playlistItems().list(
        part="snippet,contentDetails",
        maxResults=10,
        playlistId=playlist_id
    )
    response = request.execute()
    for result in response['items']:
        list_of_playlist_videoIDs_itemIDs.append({"video_id":result['contentDetails']['videoId'],
                                          "item_id":result['id']})
    return list_of_playlist_videoIDs_itemIDs


youtube = get_authenticated_service() 
try:
    with open('Intermediate/Day 46 - Music Playlist Downloader/playlist_id.txt','r') as file:
        playlist_id = file.readline() #Read playlist ID stored in text file
        list_of_playlist_videoIDs_itemIDs = get_playlist_items(youtube,playlist_id) #get existing song IDs to compare
        list_of_playlist_videoID = [item_id.get('video_id') for item_id in list_of_playlist_videoIDs_itemIDs]
        list_of_playlist_itemID = [item_id.get('item_id') for item_id in list_of_playlist_videoIDs_itemIDs]
        list_of_new_songIDs = search_songs(youtube,search_list,list_of_playlist_videoID) #get list of songs to add
        delete_song_from_playlist(youtube,list_of_new_songIDs,list_of_playlist_itemID) #delete N songs from playlist, where N is num of new songs to add
        add_song_to_playlist(youtube,playlist_id,list_of_new_songIDs) #finally add songs which are not in search_list
except FileNotFoundError as e:
    add_playlist(youtube)
except HttpError as e:
    print("Failed Request :",e.status_code)