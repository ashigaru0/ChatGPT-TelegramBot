import sqlite3
import yaml


def getChat(userId):
    con = sqlite3.connect('databases/database.db')
    cur = con.cursor()
    result = cur.execute('''SELECT name FROM chats
                            WHERE id=(
                            SELECT chats_id FROM users
                            WHERE id=?)''', (userId, )).fetchall()
    con.close()
    return [name[0] for name in result]


def getDialog(userId, name):
    con = sqlite3.connect('databases/database.db')
    cur = con.cursor()
    result = cur.execute('''SELECT dialog FROM chats
                            WHERE id=(
                            SELECT chats_id FROM users
                            WHERE id=?) AND name=?''', (userId, name)).fetchone()
    con.close()
    return yaml.safe_load(result[0]) if result != (None,) else []



