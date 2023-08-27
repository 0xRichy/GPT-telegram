from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from src.config import settings  # Assurez-vous que le chemin d'importation est correct
from src.database.telegram import telegram_api  # Assurez-vous que le chemin d'importation est correct
from src.database.telegram import telegram_commands  # Assurez-vous que le chemin d'importation est correct
from src.utils import helpers  # Assurez-vous que le chemin d'importation est correct

def main():
    # Enregistrement du message de démarrage dans la console
    helpers.log_message("Initialisation du bot Telegram...")

    # Initialisez l'API Telegram
    telegram_api_instance = telegram_api.TelegramAPI()

    # Enregistrez les commandes Telegram
    telegram_commands.register_commands(telegram_api_instance.dispatcher)

    # Démarrez le bot
    telegram_api_instance.start_bot()

    # Enregistrement du message de fin dans la console
    helpers.log_message("Bot Telegram démarré.")

if __name__ == '__main__':
    main()
