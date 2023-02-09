import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
import pandas as pd
import os
import json

#list of login info
#must all be same length
#client_ids = ["7857e62ab9094421af53b8c63e70fad9", "d258871776ff48cc87310d7ab2ec5882", "87b59c13e62f40fe8e88a5e8d691d4c4", "5cb7cba382de499bbf9f7a1a19ad4fb6"]                  
#client_secrets = ["0393d6515a334a6e8a05d081e5ee5c27",  "425770791b664857be5af72dd0918737", "3b206b365c7d45a1a54a868153f7c1b1", "861200e9587f42bd91440d6648428195"]
usernames = ["joshhall811",  "sheepran", "vals0405"]
client_id = "7857e62ab9094421af53b8c63e70fad9"               
client_secret = "0393d6515a334a6e8a05d081e5ee5c27"
# usernames = ["joshhall811"]


#for validating login
redirect_uri = "http://localhost:5000/"


#pull top tracks for each user
def main():
	output = {}
	#for i in range(len(usernames)):

	#create directory for caching user login
	caches_folder = '.spotify-caches/'
	session_path = caches_folder + "temp"
	if not os.path.exists(caches_folder):
		os.makedirs(caches_folder)
	print("cache good")
	cache_handler = spotipy.cache_handler.CacheFileHandler(cache_path=session_path)
	print("handler good")
	auth_manager = SpotifyOAuth(client_id=client_id, client_secret = client_secret, redirect_uri = redirect_uri, scope='user-top-read', cache_handler=cache_handler, show_dialog=True)
	print("auth good")
	#create authorization
	sp = spotipy.Spotify(auth_manager = auth_manager)
	print(sp.current_user())

	#pull top tracks (can pull as many as we need, currently 50)
	tracks = sp.current_user_top_tracks(50)

	#translate into list of ids of top tracks
	ids = []
	for track in tracks["items"]:
		ids.append(track["id"])

	output[usernames[i]] = ids


	#clear cache (may not be needed, idk this shit got confusing)
	os.remove(session_path)

	return output


tracks = main()
print(tracks)
#with open("tracks.json", "w") as fout:
	#son.dump(tracks, fout)

#with open("tracks.json", "r") as fin:
	#tracks = json.load(fin)

#print(tracks)
def get_song_ids(tracks):
	#convert to single list of all user song ids
	out = []
	for user in tracks:
		for track in tracks[user]:
			out.append(track)
	return out

#ids = get_song_ids(tracks) #list of groups song ids

def get_features(tracks):
	ids = []

	user_df = pd.DataFrame()
	token = util.prompt_for_user_token(username="joshhall811", scope="user-top-read", client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
	sp = spotipy.Spotify(auth = token)
	#pull all ids from main
	for user in tracks:
		print(user)
		if user_df.empty:
			feat = sp.audio_features(tracks[user])
			user_df = pd.DataFrame(feat)
			user_df["username"] = user
		else:
			feat = sp.audio_features(tracks[user])
			next_df = pd.DataFrame(feat)
			next_df["username"] = user
			user_df = pd.concat([user_df, next_df], axis = 0)
	return user_df

#pd.set_option("display.max_rows", None, "display.max_columns", None)
user_df = get_features(tracks)
#with open("user_songs.csv", "w") as fout:
	#user_df.to_csv(fout, index=False)