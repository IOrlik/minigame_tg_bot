import sqlite3
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
               id INTEGER PRIMARY KEY, 
               name TEXT,
               age INTEGER,
               like_bots TEXT
               )
 ''')
conn.commit()

def add_user(user_id, name, age, like_bots):
    cursor.execute(''' 
    INSERT INTO users (id, name, age, like_bots)
    VALUES (?, ?, ?, ?)
    ON CONFLICT(id) DO UPDATE SET
        name = excluded.name, 
        age = excluded.age,
        like_bots = excluded.like_bots
''', (user_id, name, age, like_bots))
    conn.commit()


def show_db():
    all_lines = cursor.execute('''
        SELECT * FROM users  
    ''')
    return all_lines.fetchall()

show_db()