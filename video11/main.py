# !/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from urllib.request import urlretrieve
import os
from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
import random
import data
import time
albom_id, group_id = ID ВАШЕГО АЛЬБОМА, ID ВАШЕЙ ГРУППЫ
login, password = 'ЛОГИН','ПАРОЛЬ'
vk_session = vk_api.VkApi(login, password, app_id=2685278)
vk_session.auth(token_only=True)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


def send_message(peer_id, session_api=session_api, message=None, attachment=None, keyboard=None, payload=None):
    session_api.messages.send(peer_id=peer_id, message=message, random_id=random.randint(-2147483648, +2147483648),
                              attachment=attachment, keyboard=keyboard, payload=payload)

for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            response = event.text.lower()
            if response == '/add_photo':
                try:
                    info_photos = []
                    print(event.attachments)
                    for k, v in event.attachments.items():
                        if v == 'photo':
                            info_photos.append(session_api.photos.getById(photos=event.attachments[k[:-5]]))
                    if not os.path.exists('saved'):
                        os.mkdir('saved')
                    photo_folder= 'saved'
                    for photo in info_photos:
                        now,max = 0,0
                        for i in range(len(photo[0]['sizes'])):
                            now = photo[0]['sizes'][i]['width']
                            if now > max:
                                max = now
                                n = i
                        url = photo[0]['sizes'][n]['url']
                        if not os.path.exists(os.getcwd()+"/"+photo_folder + "/" + os.path.split(url)[1]):
                            urlretrieve(url, os.getcwd()+"/"+photo_folder + "/" + os.path.split(url)[1])  # Загружаем и сохраняем файл
                    upload = vk_api.VkUpload(vk_session)
                    for element in os.listdir(path=os.getcwd()+'/'+photo_folder):
                        photo = upload.photo(
                            os.getcwd()+'/{0}/{1}'.format(photo_folder,element),
                            album_id=albom_id,
                            group_id=group_id
                        )
                        os.remove(path=os.getcwd()+'/{0}/{1}'.format(photo_folder,element))
                    print('ok')
                    send_message(peer_id=event.peer_id, message='Фотографии успешно загружены!')
                    print('отправлено')
                except Exception as er:
                    print(er)
                    send_message(message='Не удалось добавить фото в альбом группы. Произошла ошибка: {}'.format(er), peer_id=event.peer_id)
