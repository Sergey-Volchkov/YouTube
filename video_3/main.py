#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '../')

from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api
from datetime import datetime
import random
import time
import get_pictures

#login, password='login','password'
# vk_session = vk_api.VkApi(login, password)
# vk_session.auth()
token ='token'
vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()

longpoll = VkLongPoll(vk_session)


def create_keyboard(response):
    keyboard = VkKeyboard(one_time=False)

    if response == 'тест':

        keyboard.add_button('Белая кнопка', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('Зелёная кнопка', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Красная кнопка', color=VkKeyboardColor.NEGATIVE)

        keyboard.add_line()
        keyboard.add_button('Синяя кнопка', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Привет', color=VkKeyboardColor.PRIMARY)


    elif response == 'привет':
        keyboard.add_button('Тест', color=VkKeyboardColor.POSITIVE)

    elif response == 'котики':
        keyboard.add_button('Котики!', color=VkKeyboardColor.POSITIVE)

    elif response == 'закрыть':
        print('закрываем клаву')
        return keyboard.get_empty_keyboard()

    keyboard = keyboard.get_keyboard()
    return keyboard


def send_message(vk_session, id_type, id, message=None, attachment=None, keyboard=None):
    vk_session.method('messages.send',{id_type: id, 'message': message, 'random_id': random.randint(-2147483648, +2147483648), "attachment": attachment, 'keyboard': keyboard})

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
            print('Текст сообщения: ' + str(event.text))
            print(event.user_id)
            response = event.text.lower()
            keyboard = create_keyboard(response)

            if event.from_user and not event.from_me:
                if response == "котики":
                    attachment = get_pictures.get(vk_session, -130670107, session_api)
                    send_message(vk_session, 'user_id', event.user_id, message='Держи котиков!', attachment=attachment, keyboard=keyboard)
                elif response == "привет":
                    send_message(vk_session, 'user_id', event.user_id, message='Нажми на кнопку, чтобы получить список команд',keyboard=keyboard)
                elif response == "тест":
                    send_message(vk_session, 'user_id', event.user_id, message= 'Тестовые команды',keyboard=keyboard)
                elif response=='команды':
                    send_message(vk_session, 'user_id', event.user_id, message='Список команд бота: \n \n 1)Команда1 \n 2)Команда2')

                elif response=='закрыть':
                    send_message(vk_session, 'user_id', event.user_id, message='Закрыть',keyboard=keyboard)



            elif event.from_chat :
                if response == "котики":
                    attachment = get_pictures.get(vk_session, -130670107, session_api)
                    print(attachment)
                    send_message(vk_session, 'chat_id', event.chat_id, message='Держите котиков!', attachment= attachment)
            print('-' * 30)
