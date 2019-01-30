#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

sys.path.insert(0, '../')

from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api
from datetime import datetime
import random
import time
# import get_pictures
import data

login, password, token = data.d()

# vk_session = vk_api.VkApi(login, password)
# vk_session.auth()

vk_session = vk_api.VkApi(token=token)
session_api = vk_session.get_api()

longpoll = VkBotLongPoll(vk_session, 176874916)


def send_message(session_api, peer_id, message=None, attachment=None, keyboard=None, payload=None):
    session_api.messages.send(peer_id=peer_id, message=message, random_id=random.randint(-2147483648, +2147483648),
                              attachment=attachment, keyboard=keyboard, payload=payload)


while True:
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            # ДЛЯ СООБЩЕНИЙ ИЗ БЕСЕДОК
            if event.obj.peer_id != event.obj.from_id:

                # members_list = session_api.messages.getConversationMembers(peer_id=event.obj.peer_id, fields='profiles')['profiles']
                sender_name = list(filter(lambda name: name['id'] == event.obj.from_id, [name for name in session_api.messages.getConversationMembers(peer_id=event.obj.peer_id, fields='profiles')['profiles']]))[0]
                last_and_first_name = str(sender_name['first_name']) + ' ' + str(sender_name['last_name'])

                # print(members_list)
                send_message(session_api,peer_id=event.obj.peer_id, message='Привет, {0}!'.format(last_and_first_name))
                # for element in members_list:
                #     print(element['i)
                # print([[name['id'], name['first_name']] for name in members_list])
                # print(event.obj.from_id)
                # print(sender_name)
                # print(event.type)
                print(event)
                # print(event.obj)
                # print(event.object)
                # print(event.obj)
                # for key, value in event.obj.items():
                #     print(str(key) +" : " + str(value))
                print('-' * 30)
            if event.obj.peer_id == event.obj.from_id:
                print(event.type)
                print(event)
                print(event.obj)
                for key, value in event.obj.items():
                    print(str(key) + " : " + str(value))
                print('-' * 30)
