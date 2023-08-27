import sqlite3
from src.utils import helpers  # Assurez-vous que le chemin d'importation est correct

def create_table():
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, last_interaction TEXT)''')
    conn.commit()
    conn.close()
    helpers.log_message("Table 'users' créée ou déjà existante.")

def add_user(user_id, username):
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (id, username) VALUES (?, ?)", (user_id, username))
    conn.commit()
    conn.close()
    helpers.log_message(f"Utilisateur {username} ajouté.")

def update_last_interaction(user_id, timestamp):
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()
    c.execute("UPDATE users SET last_interaction = ? WHERE id = ?", (timestamp, user_id))
    conn.commit()
    conn.close()
    helpers.log_message(f"Dernière interaction de l'utilisateur {user_id} mise à jour.")

def delete_user(user_id):
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    helpers.log_message(f"Utilisateur {user_id} supprimé.")

# Exemple d'utilisation
if __name__ == "__main__":
    create_table()
    add_user(1, "Alice")
    update_last_interaction(1, "2023-08-27 12:34:56")
    delete_user(1)
