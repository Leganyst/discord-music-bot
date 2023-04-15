import vk_api

from configs import login, password

from vk_api.audio import VkAudio

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


