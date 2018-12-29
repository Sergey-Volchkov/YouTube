#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import time

def get(vk_session, id_group,vk):
    try:
        attachment = ''
        # print('До всего '+str(time.ctime(time.time())))
        max_num = vk.photos.get(owner_id=id_group, album_id='wall', count=0)['count']
        # print('Смотрим время после получения количества всех картинок ' + str(time.ctime(time.time())))
        num = random.randint(1, max_num)
        # print('Время до получения пикчи ' + str(time.ctime(time.time())))
        pictures = vk.photos.get(owner_id=str(id_group), album_id='wall', count=5, offset=num)['items']
        buf = []
        for element in pictures:
            buf.append('photo' + str(id_group) + '_' + str(element['id']))
        print(buf)
        attachment = ','.join(buf)
        print(type(attachment))
        # print('Время после получения пикчи '+str(time.ctime(time.time())))
        print(attachment)
        return attachment
    except:
        return get(vk_session, id_group, vk)