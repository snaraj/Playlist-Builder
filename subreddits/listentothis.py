from scrapper import reddit
from utility import populate_playlist
import pprint
import re

LIMIT = 50
SUBREDDIT = 'listentothis'

class listentothis():

	#object is a dictionary of songs.
	def __init__(self):
		self.songs = {}
		self.artist_list = []
		self.song_list = []

	def get_music_listentothis(self, limit):
		#grabs the subreddit, just put the name
		subreddit = reddit.subreddit(SUBREDDIT)
		
		#limit defines how many posts are gonna be used
		hot = subreddit.hot(limit = limit)
		
		#Different filter criteria than other subreddits
		#must account for specific things such as fantano reviews
		#or daily discussion posts.
		i = 1
		for submission in hot:
			if submission.title.__contains__('--') \
			or submission.title.__contains__('-'):
				self.songs.update({i : [submission.title, submission.url]})
				i+=1

		return self.songs

	def clean_list(self, list):
		newList = []
		for x in range(len(list)):
			list[x] = str(list[x])
			newList.append(re.sub('[^a-zA-Z0-9]+', ' ', list[x]).strip())

		return newList

	def get_song_list(self):
		#populate directory with the song information from get_fresh_music_indieheads
		songs_dictionary = self.get_music_listentothis(LIMIT)

		#holds a list of all of the song names.
		listOfSongNames = []

		for value in songs_dictionary.values():
			string = (str(value))
			string_with_symbols = re.findall('- (.*)\\[', string)
			listOfSongNames.append(string_with_symbols)

		return self.clean_list(listOfSongNames)

	def get_artist_list(self):
		#populate a dictionary with the song information as the value for every key
		songs_dictionary = self.get_music_listentothis(LIMIT)

		#only grab the artist of the song, and populate a list of artist.
		listOfArtist = []
		for value in songs_dictionary.values():
			x = (str(value))
			listOfArtist.append(re.findall('(.*) -', x))

		return self.clean_list(listOfArtist)