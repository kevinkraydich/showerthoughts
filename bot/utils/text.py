"""
SMS text module using Twilio API.

Kevin Kraydich <kraydich@umich.edu>
"""

import os
from dotenv import load_dotenv
from twilio.rest import Client

# Load environment variables
path = os.path.join(os.getcwd(), 'bot/', 'utils/', 'twilio.env')
load_dotenv(path)

class Text:
	def __init__(self, recipient):
		account_sid = os.environ['TWILIO_ACCOUNT_SID']
		auth_token = os.environ['TWILIO_AUTH_TOKEN']
		self._client = Client(account_sid, auth_token)
		self._recipient = recipient
		self._sender = os.environ['TWILIO_PHONE_NUMBER']

	def send(self, msg):
		self._client.messages.create(
            body = msg,
            from_ = self._sender,
            to = self._recipient
        )
