Interactive Discord Bot for Streamlined User Engagement and Automation
Overview
This Discord bot is designed to enhance user interaction within a server by responding to various predefined commands. It can respond to greetings, provide jokes, list programming languages, share its favorite subject, and fetch metadata if running on an AWS EC2 instance. The bot is easy to customize, allowing users to update the lists of jokes, programming languages, courses, and greetings by modifying simple lists and dictionaries in the code.

Features
Greeting Responses: The bot responds to different greetings with randomized messages.
Jokes: The bot can tell a random joke when prompted.
Programming Languages: The bot can list some programming languages.
Favorite Subject: The bot can share its favorite course.
EC2 Metadata: If running on an AWS EC2 instance, the bot can fetch and share instance metadata.
Setup
Prerequisites
Python 3.8+
discord.py library
python-ec2-metadata library
python-dotenv library
Installation
Clone the repository or download the script.
Install the required Python packages:
bash
Copy code
pip install discord.py python-ec2-metadata python-dotenv
Create a .env file in the same directory as the script and add your Discord bot token:
makefile
Copy code
TOKEN=your_discord_bot_token
Running the Bot
Ensure your bot is added to your Discord server.
Run the bot script:
bash
Copy code
python bot_script.py
Usage
Commands
Greetings: The bot responds to various greetings like "hello world", "hi", "hey", "greetings", and "salutations".
Jokes: Ask the bot to "tell me a joke" or "say something funny" for a random joke.
Programming Languages: Ask the bot to "tell me some programming languages" or "list programming languages" for a random programming language.
Favorite Subject: Ask the bot "what is your favorite subject" to get a response with a favorite course.
Server Metadata: Ask the bot to "tell me about my server" to fetch and display EC2 metadata (only if running on AWS EC2).
Customization
Jokes: Add or remove jokes from the JOKES list.
Languages: Add or remove programming languages from the LANGUAGES list.
Courses: Add or remove courses from the COURSES list.
Greeting Responses: Modify the GREETING_RESPONSES dictionary to change greetings and responses.
Error Handling
The bot includes error handling for common issues:

ConnectionError: Informs the user if unable to connect to the EC2 metadata service.
TimeoutError: Informs the user if the connection to the EC2 metadata service times out.
Generic Exception: Catches and displays any other unexpected errors.
Contributing
Feel free to submit issues or pull requests to improve the bot. Contributions are welcome!

License
This project is licensed under the MIT License. See the LICENSE file for details.


