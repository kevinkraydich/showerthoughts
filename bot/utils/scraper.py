"""
Scraper module using Reddit API.

Kevin Kraydich <kraydich@umich.edu>
"""

import praw
import random

reddit = praw.Reddit('my_bot')

class Scraper:
	def __init__(self, subreddit_name, max_posts):
		self.subreddit = reddit.subreddit(subreddit_name)
		self.posts = scrape_posts(self.subreddit, max_posts)

	def get_random_post(self):
		return random.choice(self.posts)

def scrape_posts(subreddit, max_posts):
	posts = []
	for submission in subreddit.hot(limit=max_posts):
		if not (submission.pinned or submission.stickied):
			posts.append(submission.title)
	return posts
