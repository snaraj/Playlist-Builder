import praw
import pprint
import json

#Set up.
# -----> get client_id and client_secret from: https://www.reddit.com/prefs/apps
# -----> Username and password are your accounts username and password 
# -----> user_agent can be anything.
reddit = praw.Reddit(client_id = '-764Hb2oqx9bqg',
					 client_secret = 'EX1afCQfdE2zGobBfP1L7ydFyks',
					 username = 'username',
					 password = 'password',
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

indieheads_songs_dictionary = get_fresh_music_indieheads(10, 'indieheads')
pp = pprint.PrettyPrinter(indent=2, width='80')
pp.pprint(indieheads_songs_dictionary)

raw_entry = json.dumps(indieheads_songs_dictionary[1])
split_entry = raw_entry.split(']')
artist_and_tittle_str = split_entry
print(artist_and_tittle_str)





























