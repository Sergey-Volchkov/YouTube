from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime

login, password = "login", "password"
vk_session = vk_api.VkApi(login=login, password=password, app_id=2685278)
vk_session.auth(token_only=True)

# token = "ЗдесьЕстьВашТокен"
# vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
            print('Текст сообщения: ' + str(event.text))
