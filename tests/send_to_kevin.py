"""
Test case that sends a text to myself.

Kevin Kraydich <kraydich@umich.edu>
"""

# Import third party modules
import os
import sys
from dotenv import load_dotenv

path = os.path.join(os.getcwd(), 'bot/')
sys.path.append(path)

# Import local modules
import bot

load_dotenv()

bot = bot.Bot()
bot.add_number(os.environ['MY_NUMBER'])

print("Sending texts")
bot.send_texts()
