import sqlite3
import time

from aiogram import types

import config
from create_bot import bot


def distribution(groups: str):
    # Сделать список групп
    res_groups = groups.split(',')

    # Собрать всех польхователей для рассылки
    list_members = []
    base = sqlite3.connect('database/members.db')
    cursor = base.cursor()
    subs_members = cursor.execute('SELECT * FROM members WHERE subs == ?', (1,)).fetchall()
    for member in subs_members:
        if str(member[2]) in res_groups:
            list_members.append(member)

    return list_members

