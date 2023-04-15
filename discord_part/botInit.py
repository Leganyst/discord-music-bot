import discord
from discord.ext import commands


# Создаем экземпляр intents с разрешениями по умолчанию
intents = discord.Intents.default()
# Включаем необходимые intents
intents.messages = True
intents.message_content = True
intents.voice_states = True
intents.guild_messages = True

# Создаем экземпляр бота с указанным intents
bot = commands.Bot(command_prefix='/', intents=intents)