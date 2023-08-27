from telegram.ext import CommandHandler, MessageHandler, Filters
from src.models import chat_model  # Assurez-vous que le chemin d'importation est correct
from src.utils import helpers  # Assurez-vous que le chemin d'importation est correct

# Initialisez le modèle de chat avec votre clé API OpenAI
api_key = "votre_clé_API_OpenAI"
chat_model_instance = chat_model.ChatModel(api_key)

def start(update, context):
    update.message.reply_text("Bonjour ! Je suis votre chatbot GPT-Telegram.")

def help_command(update, context):
    update.message.reply_text("Voici les commandes que vous pouvez utiliser:\n/start - Pour démarrer le bot\n/help - Pour obtenir de l'aide")

def echo(update, context):
    user_input = helpers.sanitize_user_input(update.message.text)
    response = chat_model_instance.get_response(user_input)
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

def register_commands(dispatcher):
    # Enregistrement des commandes
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

# Exemple d'utilisation
if __name__ == "__main__":
    from telegram.ext import Updater
    updater = Updater(token="votre_token_telegram", use_context=True)
    dispatcher = updater.dispatcher
    register_commands(dispatcher)
    updater.start_polling()
