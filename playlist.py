import requests
import json
from scrapper import *
from info import USER_ID, OAUTH_TOKEN

class Playlist:

	pp = pprint.PrettyPrinter(indent=6)


	def __init__(self):
		self.user_id = USER_ID
		self.aouth_token = OAUTH_TOKEN
		self.all_songs_info = {}

	#method in charge of creating playlists
	def create_playlist(self):
		#ALL of this information is given from: https://developer.spotify.com/console/post-playlists/
		endpoint = 'https://api.spotify.com/v1/users/{}/playlists'.format(self.user_id)

		request_body = json.dumps({
				'name' : 'Generated Playlist',
				'description' : 'This is a automatically generated playlist',
				'public' : True
		})

		response = requests.post(
				endpoint,
				data = request_body,
				headers = {
					'Content-Type' : 'application/json',
					'Authorization' : 'Bearer {}'.format(self.aouth_token)
				}
		)

		res_json = response.json()

		#Returns the playlist id
		return res_json['id']

	def get_spotify_uri(self, song_name, artist_name):

		#all taken from the spotify web API. what the query should be like
		query = 'https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20'.format(
				song_name,
				artist_name
			)

		response = requests.get(
				query,
				headers = {
					'Content-Type' : 'application/json',
					'Authorization' : 'Bearer {}'.format(self.aouth_token)
				}
			)

		#res_json contains the response when looking up the given song and artist
		res_json = response.json()
		#we only want to take the tracks (name of song)
		songs = res_json['tracks']['items']
		
		#check if the songs exists or not
		if not songs:
			uri = ''
		else:
			uri = songs[0]['uri']
			# print('found uri: ', uri, ' for song: ', songs[0]['name'])

		return uri

	#take in the data scrapped, clean it up and return a list of URI's. 
	def data_to_uri(self):
		uri = []
		#parses scrapped information to the get_spotify_uri method and finds all possible
		#URI's for songs.
		for x in range(len(get_song_name())):
			uri.append(self.get_spotify_uri(clean_list(get_song_name())[x], clean_list(get_artist_name())[x]))
		
		#gets rid of all the empty entries.
		uri_clean = [x for x in uri if x]

		return uri_clean

	def add_songs_to_playlist(self):
		uris = self.data_to_uri()
		
		playlist_id = self.create_playlist()

		request_data = json.dumps(uris)

		query = 'https://api.spotify.com/v1/playlists/{}/tracks'.format(playlist_id)
		response = requests.post(
			query,
			data = request_data,
			headers = {
				'Content-Type' : 'application/json',
				'Authorization' : 'Bearer {}'.format(self.aouth_token)
			}
		)


p1 = Playlist()
print(p1.add_songs_to_playlist())










