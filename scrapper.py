import praw
import pprint
import json
import re
from info import reddit_username, reddit_password

#Set up:
# -----> get client_id and client_secret from: https://www.reddit.com/prefs/apps
# -----> Username and password are your accounts username and password 
# -----> user_agent can be anything.
reddit = praw.Reddit(client_id = '-764Hb2oqx9bqg',
					 client_secret = 'EX1afCQfdE2zGobBfP1L7ydFyks',
					 username = reddit_username,
					 password = reddit_password,
					 user_agent = 'pythonpraw')


#finds only post with the tag [FRESH
def get_fresh_music_indieheads(limit, subreddit):
	#grabs the subreddit, just put the name
	subreddit = reddit.subreddit(subreddit)
	#limit defines how many posts are gonna be used
	hot = subreddit.hot(limit = limit)
	only_fresh_headlines = {}
	#only grab hot post that contain the substring [FRESH
	i = 1
	for submission in hot:
		if submission.title.__contains__('[FRESH'):
			only_fresh_headlines.update({i : [submission.title, submission.url]})
			i+=1

	return only_fresh_headlines

#takes in a specific limit (number of posts to search for), and subreddit to generate
#a dictionary that is needed by everything else.
def get_songs_dictionary(limit, subreddit):
	songs_dictionary = get_fresh_music_indieheads(limit, subreddit)
	return songs_dictionary

#takes in a dictionary that contains information about the song, extract only the artist.
def get_artist_name():
	#populate a dictionary with the song information as the value for every key
	songs_dictionary = get_songs_dictionary(20, 'indieheads')

	#only grab the artist of the song, and populate a list of artist.
	listOfArtist = []
	for value in songs_dictionary.values():
		x = (str(value))
		listOfArtist.append(re.findall('](.+?)-', x))


	return listOfArtist

#get the song name
def get_song_name():
	#populate directory with the song information from get_fresh_music_indieheads
	songs_dictionary = get_songs_dictionary(20, 'indieheads')

	listOfSongNames = []
	for value in songs_dictionary.values():
		x = (str(value))
		print(x)
		listOfSongNames.append(re.findall('-(.+?)"', x))

	return listOfSongNames

pp = pprint.PrettyPrinter(indent = 6)
pp.pprint(get_songs_dictionary(20, 'indieheads'))
print('\n')

pp.pprint(get_song_name())

















































