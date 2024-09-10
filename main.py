import spotipy
from spotipy.oauth2 import SpotifyOAuth
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from youtubesearchpython import VideosSearch
import time
from googleapiclient.errors import HttpError

# Credenciais
client_ID = '' # Seu client ID
client_Secret = '' # Seu client secret
redirect = 'http://localhost:8888/callback'

spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_ID, client_secret=client_Secret, redirect_uri=redirect, scope='playlist-read-private'))

id_playlist = input('Insira a ID da playlist que deseja clonar: ')
playlist = spotify.playlist(id_playlist)
faixas = playlist['tracks']['items']

# YouTube
escopo = ["https://www.googleapis.com/auth/youtube.force-ssl"] 
# force-ssl permite acesso total à conta
flow = InstalledAppFlow.from_client_secrets_file('credentials.json', escopo) # Tenha um arquivo credentials.json na pasta do projeto
flow.redirect_uri = 'http://localhost:8080/'
credenciais = flow.run_local_server(port=8080)
youtube = build('youtube', 'v3', credentials=credenciais)

def pesquisa_youtube(query, limit=1):
    videosSearch = VideosSearch(query, limit=limit)
    result = videosSearch.result()
    
    if result and 'result' in result and len(result['result']) > 0:
        return result["result"][0]["id"]
    else:
        return None
    
# Criar playlist no YouTube
titulo = playlist['name']
descricao = playlist['description']
request = youtube.playlists().insert(
    part = 'snippet, status',
    body = {
        'snippet': {
            'title': titulo,
            'description': descricao
        },
        'status': {
            'privacyStatus': 'public' # pode ser 'private' também
        }
    }
)
resposta = request.execute()
youtube_playlist_id = resposta['id']  

for item in faixas:
    faixa = item['track']
    query = f'{faixa['name']} {faixa['artists'][0]['name']}'
    video_id = pesquisa_youtube(query)
    if video_id:
        max_retries = 5
        retry_count = 0
        backoff_time = 1  # In seconds
        
        while retry_count < max_retries:
            try:
                request = youtube.playlistItems().insert(
                    part = 'snippet',
                    body = {
                        'snippet': {
                            'playlistId': youtube_playlist_id,
                            'resourceId': {
                                'kind': 'youtube#video',
                                'videoId': video_id
                            }
                        }
                    }
                )
                request = request.execute()
                print(f'Adicionando: {faixa['name']} - {faixa['artists'][0]['name']}')
                break
            except HttpError as e:
                if e.resp.status == 409 and 'SERVICE_UNAVAILABLE' in str(e):
                    retry_count += 1
                    print(f"Tentativa {retry_count} falhou. Tentando novamente em {backoff_time} segundo(s)...")
                    time.sleep(backoff_time)
                    backoff_time *= 2  # Exponential backoff
                else:
                    raise Exception("Falha ao adicionar música na playlist após várias tentativas.") 

print('Clone feito com sucesso!')
