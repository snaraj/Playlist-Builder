import requests
import json
from info import USER_ID, OAUTH_TOKEN

class Playlist:

	def __init__(self):
		self.user_id = USER_ID
		self.aouth_token = OAUTH_TOKEN

	#method in charge of creating playlists
	def create_playlist(self):
		#ALL of this information is given from: https://developer.spotify.com/console/post-playlists/
		endpoint = 'https://api.spotify.com/v1/users/{}/playlists'.format(user_id)

		request_body = json.dumps({
				'name' : 'Generated Playlist',
				'description' : 'This is a automatically generated playlist',
				'public' : false
		})

		response = requests.post(
				endpoint,
				data = request_body,
				headers = {
					'Content-Type' : 'application/json',
					'Authorization' : 'Bearer {}'.format(aouth_token)
				}
		)

		res_json = response.json()

		#Returns the playlist id
		return res_json['id']

	def get_spotify_song(self, song_name, artist_name):

		query = 'https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20'.format(
				song_name,
				artist_name
			)

		response = requests.get(
				query,
				headers = {
					'Content-Type' : 'application/json',
					'Authorization' : 'Bearer {}'.format(aouth_token)
				}
			)

		res_json = response.json()
		songs = response_json['tracks']['items']

		uri = songs[0]['uri']
		
		return uri

	#def add_songs_to_playlist(self):
		#populate songs into dictionary

		#collect all of uri

		#create a new playlist

		#add all songs to the playlist















