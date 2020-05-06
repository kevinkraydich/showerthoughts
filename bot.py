import os
import praw
import random
from dotenv import load_dotenv
from twilio.rest import Client

class Scraper:
	def __init__(self):
		reddit = praw.Reddit('my_bot')
		self.subreddit = reddit.subreddit('showerthoughts')
		self.thoughts = []
		self.gather_thoughts()

	def gather_thoughts(self):
		for submission in self.subreddit.hot(limit = 10):
			if not (submission.pinned or submission.stickied):
				self.thoughts.append(submission.title)

	def random_thought(self):
		return random.choice(self.thoughts)

class Text:
	def __init__(self, to_num='', from_num=''):
		load_dotenv()
		account_sid = os.environ['TWILIO_ACCOUNT_SID']
		auth_token = os.environ['TWILIO_AUTH_TOKEN']
		self.client = Client(account_sid, auth_token)

		if to_num:
			self.recipient = to_num
		else:
			recipient = os.environ['MY_NUMBER']

		if from_num:
			self.sender = from_num
		else:
			self.sender = os.environ['TWILIO_PHONE_NUMBER']

	def send(self, msg):
		message = self.client.messages.create(
                	body = msg,
                    from_ = self.sender,
                    to = self.recipient
                )

scraper = Scraper()
contents = scraper.random_thought()
numbers = [os.environ["MY_NUMBER"]]
for num in numbers:
	msg = Text(num, '')
	msg.send(contents)