#!/usr/bin/env python
# -*- coding: utf-8 -*-
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
import time
from datetime import datetime, timedelta

login, password = 'login', 'password'
vk_session = vk_api.VkApi(login, password)
vk_session.auth()
vk = vk_session.get_api()

longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        print('Сообщение пришло в: ' + str(event.datetime + timedelta(hours=3)))
        print('Текст сообщения: ' + str(event.text))
        print(event.peer_id)

        response = event.text.lower()
        if event.from_chat or event.from_user:
            try:
                if response == '/status' or response == '/статус':

                    today = datetime.strftime(datetime.now(), "%d%m%Y")
                    tomorrow = datetime.strftime(datetime.now() + timedelta(days=1), "%d%m%Y")

                    vk.messages.send(
                        peer_id=event.peer_id,
                        random_id=random.randint(-2147483648, +2147483648),
                        message='Всего сообщений в данном диалоге : ' +
                                str(vk.messages.search(peer_id=event.peer_id, date=tomorrow, count=1)['count'] + 1) + '\nЗа сегодня: ' +
                                str( vk.messages.search(peer_id=event.peer_id, date=tomorrow, count=1)['count'] + 1 - vk.messages.search(peer_id=event.peer_id, date=today, count=1)['count'] + 1),
                    )
                elif response.split(' ')[0] == '/add':
                    print(vk.messages.getChat(chat_id=event.chat_id)['admin_id'])
                    if vk.messages.getChat(chat_id=event.chat_id)['admin_id'] == event.user_id:
                        try:
                            vk.messages.addChatUser(chat_id=event.chat_id, user_id=response.split(' ')[1])
                        except:
                            vk.messages.send(
                                peer_id=event.peer_id,
                                random_id=random.randint(-2147483648, +2147483648),
                                message='Ошибка при добавлении пользователя.'
                            )
                    else:
                        vk.messages.send(
                            peer_id=event.peer_id,
                            random_id=random.randint(-2147483648, +2147483648),
                            message='Вы не можете провести добавление участника таким способом, так как не являетесь создателем беседы.'
                        )

                elif response.split(' ')[0] == '/kick':
                    print(vk.messages.getChat(chat_id=event.chat_id)['admin_id'])
                    if vk.messages.getChat(chat_id=event.chat_id)['admin_id'] == event.user_id:
                        try:
                            vk.messages.removeChatUser(chat_id=event.chat_id, user_id=response.split(' ')[1])
                        except:
                            vk.messages.send(
                                peer_id=event.peer_id,
                                random_id=random.randint(-2147483648, +2147483648),
                                message='Ошибка при удалении пользователя.'
                            )
                    else:
                        vk.messages.send(
                            peer_id=event.peer_id,
                            random_id=random.randint(-2147483648, +2147483648),
                            message='Вы не можете провести удаление участника таким способом, так как не являетесь создателем беседы.'
                        )
                elif response == '/time':
                    vk.messages.send(
                        peer_id=event.peer_id,
                        random_id=random.randint(-2147483648, +2147483648),
                        message='Текущее время : ' + str(event.datetime + timedelta(hours=3))
                    )
            except:
                pass

            finally:
                time.sleep(3)
