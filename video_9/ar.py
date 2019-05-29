import sys

sys.path.insert(0, '../')
from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api, random
import data
login, password = data.d()


vk_session = vk_api.VkApi(login=login, password=password, app_id=2685278)
vk_session.auth(token_only=True)


session_api = vk_session.get_api()

longpoll = VkLongPoll(vk_session)

def send_message(peer_id, message=None, attachment=None, keyboard=None, payload=None):
    session_api.messages.send(peer_id=peer_id, message=message, random_id=random.randint(-2147483648, +2147483648),
                              attachment=attachment, keyboard=keyboard, payload=payload)
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        print('Текст сообщения: ' + str(event.text))
        response = event.text.lower()
        if response =='привет':
            send_message(peer_id=event.peer_id,message='Привет!')