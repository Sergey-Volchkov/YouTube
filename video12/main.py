# !/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
import random
login, password = login, password
vk_session = vk_api.VkApi(login, password, app_id=2685278)
vk_session.auth(token_only=True)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


class SetUnicVariables():
    def __init__(self, response):
        self.count = 0
        self.response = response

    def send_message(self, peer_id, session_api=session_api, message=None, attachment=None, keyboard=None, payload=None):
        session_api.messages.send(peer_id=peer_id, message=message, random_id=random.randint(-2147483648, +2147483648),
                                  attachment=attachment, keyboard=keyboard, payload=payload)
    def counter(self,event):
        self.event = event
        self.count += 1
        full_name = session_api.users.get(user_ids=session_api.messages.getById(message_ids=self.event.message_id)['items'][0]['from_id'])
        session_api.messages.send(message='Переменная-счётчик для пользователя '+
                                          str(full_name[0]['id']) + ' ' +
                                          full_name[0]['first_name'] + ' ' +
                                          full_name[0]['last_name'] +' : '+ str(self.count),
                                  random_id=random.randint(-2147483648, +2147483648), peer_id=self.event.peer_id)

users = {}
while True:
    try:
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                response = event.text.lower()
                user_id = session_api.messages.getById(message_ids=event.message_id)['items'][0]['from_id']

                if users.get(user_id)==None:
                    users[user_id] = SetUnicVariables(response)

                if response == '+1':
                    users[user_id].counter(event)

    except Exception as error:
        print(error)
