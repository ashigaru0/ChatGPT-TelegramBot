import sqlite3


async def addUser(userId):
    con = sqlite3.connect('databases/database.db')
    cur = con.cursor()
    result = cur.execute('''SELECT id FROM users
                            WHERE id=?''', (userId,)).fetchall()
    if not result:
        cur.execute('''INSERT INTO users(id) VALUES(?)''', (userId,))
    con.commit()
    con.close()


async def addChat(userId, name):
    con = sqlite3.connect('databases/database.db')
    cur = con.cursor()
    chatsId = cur.execute('''SELECT chats_id FROM users
                             WHERE id=?''', (userId,)).fetchone()
    cur.execute('''INSERT INTO chats(id, name) VALUES(?, ?)''', (chatsId[0], name))
    con.commit()
    con.close()


async def addDialog(userId, name, dialog):
    con = sqlite3.connect('databases/database.db')
    cur = con.cursor()
    chatsId = cur.execute('''SELECT chats_id FROM users
                                 WHERE id=?''', (userId,)).fetchone()
    cur.execute('''UPDATE chats
                   SET dialog = ?
                   WHERE id = ? AND name = ?''', (f"{dialog}", chatsId[0], name))
    con.commit()
    con.close()
