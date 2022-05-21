import sqlite3

from aiogram import types


def create_db(admin_id, group_id):
    base = sqlite3.connect('database/members.db')
    cursor = base.cursor()

    base.execute('CREATE TABLE IF NOT EXISTS members(id PRIMARY KEY, subs, group_id)')
    try:
        cursor.execute('INSERT INTO members VALUES(?, ?, ?)', (admin_id, 1, group_id))
        base.commit()
    except:
        pass
    base.close()


def add_member(user_id, group_id):
    base = sqlite3.connect('database/members.db')
    cursor = base.cursor()

    try:
        cursor.execute('INSERT INTO members VALUES(?, ?, ?)', (user_id, 0, group_id))
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


def print_members(group_id):
    base = sqlite3.connect('members.db')
    cursor = base.cursor()

    res = cursor.execute('SELECT * FROM members').fetchall()
    print(res)


def subs(user_id):
    base = sqlite3.connect('database/members.db')
    cursor = base.cursor()

    cursor.execute('UPDATE members SET subs == ? WHERE id == ?', (1, user_id))
    base.commit()
    base.close()


def unsubs(user_id):
    base = sqlite3.connect('database/members.db')
    cursor = base.cursor()

    cursor.execute('UPDATE members SET subs == ? WHERE id == ?', (0, user_id))
    base.commit()
    base.close()


if __name__ == '__main__':
    print_members('-1001556943381')
