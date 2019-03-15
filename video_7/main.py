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
import get_pictures


vk_session = vk_api.VkApi(token='')
session_api = vk_session.get_api()

# longpoll = VkBotLongPoll(vk_session, group_id)


def send_message(peer_id, message=None, attachment=None, keyboard=None, payload=None):
    session_api.messages.send(peer_id=peer_id, message=message, random_id=random.randint(-2147483648, +2147483648),
                              attachment=attachment, keyboard=keyboard, payload=payload)

attachment = get_pictures.get()

print(attachment)
send_message(attachment=attachment,peer_id='')