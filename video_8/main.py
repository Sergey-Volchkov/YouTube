import sys

sys.path.insert(0, '../')

from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api, random, time,os
import data
token, group_id = data.f()
vk_session = vk_api.VkApi(token=token)
session_api = vk_session.get_api()

longpoll = VkBotLongPoll(vk_session, group_id)



def send_message(peer_id, message=None, attachment=None, keyboard=None, payload=None):
    session_api.messages.send(peer_id=peer_id, message=message, random_id=random.randint(-2147483648, +2147483648),
                              attachment=attachment, keyboard=keyboard, payload=payload)


def create_keyboard(payload):
    keyboard = vk_api.keyboard.VkKeyboard(one_time=True)
    if payload != None:
        keyboard.add_button('Рассказать о рыбалке', payload=2, color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Рассказать о машинах', payload=3, color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Рассказать о моде', payload=4, color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Рассказать о животных', payload=5, color=VkKeyboardColor.PRIMARY)
    else:
        keyboard.add_button('Начать!', payload=1, color=VkKeyboardColor.POSITIVE)
    return keyboard.get_keyboard()


for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        print('Текст сообщения: ' + str(event.obj.text))
        if event.obj.payload != None:
            payload = int(event.obj.payload)
        else:
            payload = None

        response = event.obj.text.lower()
        if not event.obj.from_me:

            keyboard = create_keyboard(payload)
            if response == 'начать!' or payload==1:
                send_message(peer_id=event.obj.peer_id,message='О чем ты хочешь узнать?',keyboard=keyboard)
            elif payload==None:
                send_message(peer_id=event.obj.peer_id,message='Нажми на кнопку чтобы начать общение с ботом!',keyboard=keyboard)
            elif payload ==2:
                send_message(peer_id=event.obj.peer_id,message='Тут могла бы быть информация о рыбалке',keyboard=keyboard)
            elif payload ==3:
                send_message(peer_id=event.obj.peer_id,message='Здесь размещена информация о машинах',keyboard=keyboard)
            else:
                send_message(peer_id=event.obj.peer_id,message='Рассказать о чём то ещё?',keyboard=keyboard)
