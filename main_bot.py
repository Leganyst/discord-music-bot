# вк токен - vk_token = 'vk1.a.VgCpPyQSLoMmZtlAjTT3cVTaSPO1fXOw0pmS1PeWdeylm6fwFqencH6DdWmvDt3gZMBLR7poGhblQlzcBTurxps9vE6N65mLdpgN_WPQgI36P3hq7eRZioFh0AZ8uj4NR4cm-V1ABG52fKxLl-KPrJMTjP_JgOQRoX0L1O12fpGyulE-Olf2KJKrjcohTnYtmDflOYkAFkJWsBk02Nla1w'
# dis токен - 'MTA5NjEyMjkxMzg3NjM1MzE1NA.GFf30I.PbYm7myPr4M4ibmJAYBYSS0alU8sJ2tOSQxdCg'

# Импортируем необходимые библиотеки
import discord
from discord.ext import commands
import asyncio
import requests
import json
import random
import vk_api

from vk_api.audio import VkAudio

# Создаем экземпляр intents с разрешениями по умолчанию
intents = discord.Intents.default()
# Включаем необходимые intents
intents.messages = True
intents.message_content = True
intents.voice_states = True
intents.guild_messages = True
# Создаем экземпляр бота с указанным intents
bot = commands.Bot(command_prefix='/', intents=intents)

# Создаем переменную для хранения токена Вконтакте
# vk_token = 'токен вк'
login = 'Логин вк'
password = 'Пароль вк'

# Создаем сессию ВК и авторизуемся
vk_session = vk_api.VkApi(login=login, password=password)
vk_session.auth()


# Создаем функцию для логина в ВК и включения музыки по ссылке или названию
def play_vk_music(url_or_name):
  # Задаем логин и пароль для ВК

  
  # Получаем доступ к API ВК
  vk = vk_session.get_api()
  
  # Получаем доступ к аудио ВК
  vk_audio = VkAudio(vk_session)
  
  # Проверяем, является ли аргумент ссылкой или названием
  if url_or_name.startswith('https://'):
    # Если это ссылка, то пытаемся получить аудио по ней
    audio = vk_audio.get_by_id(url_or_name)
  else:
    # Если это название, то пытаемся найти аудио по нему
    audio = vk_audio.search(q=url_or_name, count=1)
  
  # Проверяем, нашли ли мы аудио
  if audio:
    for aud in audio:
      # Если нашли, то получаем ссылку на mp3 файл
      mp3_url = aud['url']

      # Возвращаем ссылку на mp3 файл
      return mp3_url
  
  else:
    # Если не нашли, то возвращаем None
    return None


# Создаем функцию для дискорд бота, которая реагирует на команду /play
@bot.command()
async def play(ctx, *, url_or_name):
  # Получаем ссылку на mp3 файл из функции play_vk_music
  mp3_url = play_vk_music(url_or_name)
  
  # Проверяем, получили ли мы ссылку на mp3 файл
  if mp3_url:
    # Если получили, то проверяем, подключен ли бот к голосовому каналу
    if ctx.voice_client:
      # Если подключен, то останавливаем текущий трек и включаем новый по ссылке
      ctx.voice_client.stop()
      ctx.voice_client.play(discord.FFmpegPCMAudio(mp3_url))
      
      # Отправляем сообщение о том, что трек включен
      await ctx.send(f'Playing {url_or_name}')
    
    else:
      # Если не подключен, то пытаемся подключиться к голосовому каналу автора сообщения
      channel = ctx.author.voice.channel
      
      if channel:
        # Если автор сообщения подключен к голосовому каналу, то подключаемся к нему и включаем трек по ссылке
        await channel.connect()
        ctx.voice_client.play(discord.FFmpegPCMAudio(mp3_url))
        
        # Отправляем сообщение о том, что трек включен
        await ctx.send(f'Playing {url_or_name}')
      
      else:
        # Если автор сообщения не подключен к голосовому каналу, то отправляем сообщение об ошибке
        await ctx.send('You are not connected to a voice channel')
  
  else:
    # Если не получили ссылку на mp3 файл, то отправляем сообщение об ошибке
    await ctx.send('Could not find or play the audio')


# Создаем команду /off для выключения музыки
@bot.command()
async def off(ctx):
    # Проверяем, что бот подключен к голосовому каналу
    if bot.voice_clients:
        # Получаем экземпляр голосового клиента
        voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
        # Останавливаем воспроизведение аудио
        voice_client.stop()
        # Отключаемся от голосового канала
        await voice_client.disconnect()
        # Отправляем сообщение о том, что музыка выключена
        await ctx.send('Музыка выключена!')
    # Иначе отправляем сообщение о том, что бот не в голосовом канале
    else:
        await ctx.send('Бот не в голосовом канале!')


# Создаем команду /about для вывода информации о боте
@bot.command()
# Добавляем декоратор для проверки разрешения на отправку сообщений
@commands.has_permissions(send_messages=True)
async def about(ctx):
    # Формируем текст с информацией о боте
    info = 'Это бот для воспроизведения музыки из Вконтакте в дискорд. Создан с помощью Bing. Доступные команды:\n'
    info += '/play <параметр> - включает музыку из Вконтакте по параметру. Параметр может быть ссылкой на альбом, плейлист, трек или названием трека.\n'
    info += '/off - выключает музыку.\n'
    info += '/about - выводит информацию о боте.'
    # Отправляем сообщение с информацией о боте
    await ctx.send(info)


# Запускаем бота с вашим токеном дискорда
bot.run('Токен дс бота')
