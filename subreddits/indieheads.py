import re
from scrapper import reddit
from utility import populate_playlist

LIMIT = 50
SUBREDDIT = 'indieheads'

class indie_heads_playlist():
	
	#playlist object is a simple dictionary, where the keys are integers,
	#and the values are the headline of the reddit post being selected.
	def __init__(self):
		#Dictionary for all songs.
		self.songs = {}
		self.artist_list = []
		self.song_list = []

	def get_fresh_music_indieheads(self, limit):
		#grabs the subreddit, just put the name
		subreddit = reddit.subreddit(SUBREDDIT)
		
		#limit defines how many posts are gonna be used
		hot = subreddit.hot(limit = LIMIT)
		
		#only grab hot post that contain the substring [FRESH
		i = 1
		for submission in hot:
			if submission.title.__contains__('[FRESH'):
				self.songs.update({i : [submission.title, submission.url]})
				i+=1

		return self.songs

	#takes in a dictionary that contains information about the song, extract only the artist.
	def get_artist_list(self):
		#populate a dictionary with the song information as the value for every key
		songs_dictionary = self.get_fresh_music_indieheads(LIMIT)

		#only grab the artist of the song, and populate a list of artist.
		listOfArtist = []
		for value in songs_dictionary.values():
			x = (str(value))
			listOfArtist.append(re.findall('](.+?)-', x))


		return self.clean_list(listOfArtist)

	#get the song name
	def get_song_list(self):
		#populate directory with the song information from get_fresh_music_indieheads
		songs_dictionary = self.get_fresh_music_indieheads(LIMIT)

		listOfSongNames = []
		for value in songs_dictionary.values():
			string = (str(value))
			string_with_symbols = re.findall('-.+?,', string)
			listOfSongNames.append(string_with_symbols)

		return self.clean_list(listOfSongNames)

	#This function removes everything that isn't a letter or number and also strips
	#the whitespace at both sides of the each entry, in otherwords, this function makes it
	#it so we send acurate infomation to the spotify web api.
	def clean_list(self, list):
		newList = []
		for x in range(len(list)):
			list[x] = str(list[x])
			newList.append(re.sub('[^a-zA-Z0-9]+', ' ', list[x]).strip())

		return newList



