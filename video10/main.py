# !/usr/bin/env python
# -*- coding: utf-8 -*-
from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
import random
#import data
#login, password = data.data('user')
login, password='YOUR LOGIN', 'YOUR PASSWORD'
vk_session = vk_api.VkApi(login, password, app_id=2685278)
vk_session.auth(token_only=True)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
def send_message(peer_id, session_api=session_api, message=None, attachment=None, keyboard=None, payload=None):
    session_api.messages.send(peer_id=peer_id, message=message, random_id=random.randint(-2147483648, +2147483648),
                              attachment=attachment, keyboard=keyboard, payload=payload)
for event in longpoll.listen():
    try:
        if event.type == VkEventType.MESSAGE_NEW:
            response = event.text.lower()
            if response == '/удалить' and event.from_me:
                max_messages = session_api.messages.getHistory(user_id=event.peer_id)['count']
                text = []
                for i in range(0, max_messages, 200):
                    mess = session_api.messages.getHistory(user_id=event.peer_id, count=200, offset=i)['items']
                    for element in mess:
                        if element.get('action') == None:
                            text.append( str(element['id']))
                text = ','.join(text)
                print(text)
                session_api.messages.delete(delete_for_all=1, message_ids=text)
    except Exception as error: print(error)
