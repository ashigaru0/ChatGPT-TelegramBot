import sqlite3


async def deleteChat(userId, name):
    con = sqlite3.connect('databases/database.db')
    cur = con.cursor()
    cur.execute('''DELETE FROM chats WHERE name=? AND
                   id=(SELECT chats_id FROM users
                   WHERE id=?)''', (name, userId))
    con.commit()
    con.close()
