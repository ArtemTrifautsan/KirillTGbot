import sqlite3

from aiogram import types


def add_member(user_id):
    base = sqlite3.connect('database/members.db')
    cursor = base.cursor()

    base.execute('CREATE TABLE IF NOT EXISTS members(id PRIMARY KEY)')

    try:
        cursor.execute('INSERT INTO members VALUES(?)', (user_id,))
        base.commit()
        print(f'Пользователь с id {user_id} записан')
    except Exception as ex:
        print(ex)
    base.close()


def delete_member(user_id):
    base = sqlite3.connect('database/members.db')
    cursor = base.cursor()

    try:
        cursor.execute('DELETE FROM members WHERE id == ?', (user_id,))
        base.commit()
        print(f'Пользователь с id {user_id} удалён')
    except Exception as ex:
        print('Ошибка базы данных: ', ex)
    base.close()


def print_members():
    base = sqlite3.connect('members.db')
    cursor = base.cursor()
    base.execute('CREATE TABLE IF NOT EXISTS members(id PRIMARY KEY)')

    res = cursor.execute('SELECT * FROM members').fetchall()
    print(res)


def make_distribution(groups):
    base = sqlite3.connect('members.db')
    cursor = base.cursor()
    base.execute('CREATE TABLE IF NOT EXISTS members(id PRIMARY KEY)')

    list_members = []   # Окончательный список людей, получивших рассылку

    res = cursor.execute('SELECT * FROM members').fetchall()    # Список людей из базы данных
    """for group in groups:
        for member in res:
            member = member[0]
            type_member = types.Chat.get_member(member)
            return type_member"""
    member = res[0][0]
    return types.Chat.get_member(user_id=member)


if __name__ == '__main__':
    print_members()
    # make_distribution(17)
