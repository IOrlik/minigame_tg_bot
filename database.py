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


# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS users_characters (
#                id INTEGER PRIMARY KEY AUTOINCREMENT, 
#                user_id INTEGER, 
#                character_class CLASS
#                )
#  ''')
# conn.commit()

# def add_users_character(user_id, character_class):
#     cursor.execute(''' 
#     INSERT INTO users_characters(id, user_id, character_class)
#     VALUES (?, ?, ?)
#     ON CONFLICT(id) DO UPDATE SET 
#         user_id = excluded.user_id,
#         character_class = excluded.character_class
# ''', (user_id, character_class))
#     conn.commit()

# def get_users_character(user_id):
#     users_characters = cursor.execute(''' 
#     SELECT character_class FROM users_characters WHERE user_id = ? 
# ''', (user_id,))
#     return users_characters.fetchall()



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