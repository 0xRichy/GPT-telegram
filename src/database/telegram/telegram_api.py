from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from src.config import settings  # Assurez-vous que le chemin d'importation est correct
from src.utils import helpers  # Assurez-vous que le chemin d'importation est correct

class TelegramAPI:
    def __init__(self):
        # Enregistrement du message d'initialisation dans la console
        helpers.log_message("Initialisation de l'API Telegram...")

        self.token = settings.TELEGRAM_API_TOKEN
        self.updater = Updater(token=self.token, use_context=True)
        self.dispatcher = self.updater.dispatcher

    def add_command_handler(self, command, callback):
        self.dispatcher.add_handler(CommandHandler(command, callback))

    def add_message_handler(self, callback):
        self.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, callback))

    def start_bot(self):
        # Enregistrement du message de démarrage dans la console
        helpers.log_message("Démarrage du bot Telegram...")
        
        self.updater.start_polling()
        self.updater.idle()

        # Enregistrement du message de fin dans la console
        helpers.log_message("Bot Telegram arrêté.")

    def send_message(self, chat_id, text):
        bot = Bot(token=self.token)
        bot.send_message(chat_id=chat_id, text=text)

# Exemple d'utilisation
if __name__ == "__main__":
    def start(update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text="Je suis votre chatbot!")

    def echo(update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

    telegram_api = TelegramAPI()
    telegram_api.add_command_handler('start', start)
    telegram_api.add_message_handler(echo)
    telegram_api.start_bot()
