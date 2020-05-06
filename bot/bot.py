"""
Python module for Reddit bot.

Kevin Kraydich <kraydich@umich.edu>
"""

# Import third party modules
import os
import configparser
import sys

path = os.path.join(os.getcwd(), 'bot/', 'utils/')
sys.path.append(path)

# Import local modules
import scraper
import text

config = configparser.ConfigParser()
settings_path = os.path.join(os.getcwd(), 'bot/', 'settings.ini')
config.read(settings_path)

class Bot:
	def __init__(self):
		subreddit = config.get('default', 'subreddit_name')
		num_posts = config.getint('default', 'max_posts')
		print("Loading scraper")
		self._scraper = scraper.Scraper(subreddit, num_posts)
		self._numbers = []
	
	def add_number(self, num):
		self._numbers.append(num)
		
	def send_texts(self):
		print("Grabbing random showerthought")
		contents = self._scraper.get_random_post()
		for num in self._numbers:
			msg = text.Text(num)
			msg.send(contents)
