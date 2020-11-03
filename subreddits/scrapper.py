import sys
sys.path.append('C:/Users/Samuel/Documents/Programming/Python/Playlist_Builder/music_scraper/setup')
from info import reddit_username, reddit_password
import praw

reddit = praw.Reddit(client_id = '-764Hb2oqx9bqg',
					 client_secret = 'EX1afCQfdE2zGobBfP1L7ydFyks',
					 username = reddit_username,
					 password = reddit_password,
					 user_agent = 'pythonpraw')




















