import datetime

def get_current_time():
    """
    Retourne l'heure actuelle au format HH:MM:SS
    """
    return datetime.datetime.now().strftime("%H:%M:%S")

def sanitize_user_input(user_input):
    """
    Nettoie l'entrée utilisateur en supprimant les espaces inutiles et en convertissant le texte en minuscules
    """
    return user_input.strip().lower()

def log_message(message, level="INFO"):
    """
    Enregistre un message dans la console avec un niveau de gravité (INFO, WARNING, ERROR)
    """
    current_time = get_current_time()
    print(f"[{current_time}] [{level}] {message}")

# Exemple d'utilisation
if __name__ == "__main__":
    print(get_current_time())  # Output: "HH:MM:SS"
    print(sanitize_user_input("  Bonjour  "))  # Output: "bonjour"
    log_message("Ceci est un message de test.")  # Output: "[HH:MM:SS] [INFO] Ceci est un message de test."
