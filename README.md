# VK Music Bot for Discord

VK Music Bot is a Discord bot that allows you to play music from VKontakte (VK) through your own VK account. You can search for songs by name or URL and play them in a voice channel. VK Music Bot also supports pausing and resuming the playback.

## Features

- Play music from VK using your own VK account
- Search for songs by name or URL
- Get information about the bot with /about command

## Installation

To install VK Music Bot, you need to have Python 3.7 or higher and pip installed on your system. You also need to have a VK account with some music in it. Follow these steps:

- Clone this repository or download the zip file and extract it
- Open a terminal and navigate to the folder where you cloned or extracted the bot
- Run `pip install -r requirements.txt` to install the dependencies
- Edit configs.py:
  - `TOKEN` is your Discord bot token. You can get it from the [Discord Developer Portal](https://discord.com/developers/applications)
  -  Input `LOGIN` and `PASSWORD` when running the file
- Run `python main_bot.py` to start the bot
- Invite the bot to your Discord server using this link: https://discord.com/api/oauth2/authorize?client_id={your_client_id}&permissions=8&scope=bot
  - Replace `CLIENT_ID` with your Discord bot client ID. You can get it from the [Discord Developer Portal](https://discord.com/developers/applications)

## Usage

To use VK Music Bot, you need to be in a voice channel and have permission to manage messages. You can use the following commands:

- `/play <query>`: Play a song by name or URL. If a song is already playing, stop it and play the new one.
- `/off`: Stop the playback and leave the voice channel.
- `/about`: Show information about the bot and its author.

## Contact

If you have any questions, suggestions, or issues with VK Music Bot, please contact me `@legannyst` in Telegram or open an issue on GitHub.
