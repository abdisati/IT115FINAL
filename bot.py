import discord
import os
import random
from ec2_metadata import ec2_metadata
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Get the bot token from environment variables
TOKEN = os.getenv('TOKEN')

# Initialize bot with specified intents
intents = discord.Intents.default()
intents.message_content = True  # Enable the message content intent
client = discord.Client(intents=intents)

# List of jokes
JOKES = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Parallel lines have so much in common. It's a shame they'll never meet.",
    "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    "I'm reading a book on the history of glue. I just can't seem to put it down!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
]

# List of potential responses
LANGUAGES = ["CSS", "HTML", "JAVA", "JavaScript"]
COURSES = ["IT115", "IT116"]

# Dictionary for defining greetings and responses
GREETING_RESPONSES = {
    "hello world": ["Hello", "Hi there!", "Hey!"],
    "hi": ["Hello!", "Hey there!", "Hi!"],
    "hey": ["Hey", "Hello!", "Hi there!"],
    "greetings": ["Greetings!", "Hello!", "Hi"],
    "salutations": ["Salutations!", "Hello!", "Greetings!"]
}


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

    # Convert the message content to lowercase for case-insensitive matching
    message_content = message.content.lower()
    # Print message details
    print(f'Message "{message.content}" by {message.author.name} in channel "{message.channel.name}"')

    # Check if the message is a greeting and respond accordingly
    for greeting in GREETING_RESPONSES:
        if greeting in message_content:
            response = random.choice(GREETING_RESPONSES[greeting])
            await message.channel.send(f"{response} {message.author.name}")
            break

    # Respond with a joke if message contains "tell me a joke"
    if "tell me a joke" in message_content or "say something funny" in message_content:
        await message.channel.send(random.choice(JOKES))
    #Respond with name of some programming languages if "tell me some programming languages" is message content
    elif "tell me some programming languages" in message_content or "list programming languages" in message_content:
        await message.channel.send(random.choice(LANGUAGES))
    #Respond to "what is your favorite " subject 
    elif "what is your favorite subject" in message_content:
        await message.channel.send(random.choice(COURSES))
    #Respond to "Tell me about my server"
    elif "ec2 tell me about my server" in message_content:
        try:
            #Attempt to fetch EC2 metadata
            instance_id = ec2_metadata.instance_id
            instance_type = ec2_metadata.instance_type
            availability_zone = ec2_metadata.availability_zone
            metadata_str = f"EC2 Instance ID: {instance_id}, Instance Type: {instance_type}, Availability Zone: {availability_zone}"
            #Send metadata informatin to the Discord chanel
            await message.channel.send(metadata_str)
            # Catch ConnectionError if unable to connect to EC2 metadata service
        except ConnectionError:
             # Inform the user about the connection issue
            await message.channel.send("Error: Unable to connect to EC2 metadata service.")
            # Catch TimeoutError if connection to EC2 metadata service times out
        except TimeoutError:
              # Inform the user about the timeout issue
            await message.channel.send("Error: Connection to EC2 metadata service timed out.")
            # Catch any other unexpected exceptions
        except Exception as e:
            await message.channel.send(f"Error fetching EC2 metadata: {e}")

# Run the bot using the token from the environment variables
try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print(f"Error logging in: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
