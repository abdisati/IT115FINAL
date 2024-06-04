
import discord
import os
import random
from dotenv import load_dotenv
import re

# Load environment variables from a .env file
load_dotenv()

# Get the bot token from environment variables
token = os.getenv('TOKEN')

# Initialize bot as a discord.Client
intents = discord.Intents.default()
intents.message_content = True  # Enable the message content intent
client = discord.Client(intents=intents)

# List of jokes
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Parallel lines have so much in common. It's a shame they'll never meet.",
    "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    "I'm reading a book on the history of glue. I just can't seem to put it down!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
]

# List of profanity words to censor
profanity = ["fuck", "shit", "asshole", "bitch", "damn", "Get the fuck out of here"]

# List of GIF emojis to send as responses
curse = [
    "Fuck you",
    "Bitch",
    "Motherfucker",
]

instructor=["I think is dan", "Monte may be", "I like greg", "dr p lol"]

coarse = ["IT115", "IT116"]


# Event triggered when the bot is ready
@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

# Event triggered when a message is sent in any channel
@client.event
async def on_message(message):
    # Ignore messages sent by the bot itself to prevent loops
    if message.author == client.user:
        return

    # Check for profanity and censor it
    content = message.content.lower()
    for word in profanity:
        content = re.sub(rf'\b{word}\b', '*' * len(word), content)

    # Respond with a joke if message contains "tell me a joke"
    if "tell me a joke" in content or "say something funny" in content:
        await message.channel.send(random.choice(jokes))
    elif "who is the best instructor" in content or "who is the best teacher" in content:
        # Respond with a GIF emoji
        await message.channel.send(random.choice(instructor))
    elif "what is your favorite subject" in content:
        await message.channel.send(random.choice(coarse))
    else:
        await message.channel.send(random.choice(curse))

# Run the bot using the token from the environment variables
client.run(token)
