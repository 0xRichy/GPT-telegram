from telegram.ext import CommandHandler, MessageHandler, Filters
from src.models import chat_model  # Assurez-vous que le chemin d'importation est correct
from src.config import settings  # Assurez-vous que le chemin d'importation est correct
from src.utils import helpers  # Assurez-vous que le chemin d'importation est correct

# Initialisez le modèle de chat avec votre clé API OpenAI
chat_model_instance = chat_model.ChatModel()

def start(update, context):
    update.message.reply_text("Bonjour ! Je suis votre chatbot GPT-Telegram.")

def help_command(update, context):
    update.message.reply_text("Voici les commandes que vous pouvez utiliser:\n/start - Pour démarrer le bot\n/help - Pour obtenir de l'aide")

def update_openai_token(update, context):
    new_token = update.message.text.split(' ')[1]  # Extrait le nouveau token de la commande
    settings.update_openai_api_token(new_token)
    update.message.reply_text(f"Token de l'API OpenAI mis à jour : {new_token}")

def echo(update, context):
    user_input = helpers.sanitize_user_input(update.message.text)
    response = chat_model_instance.get_response(user_input)
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

def register_commands(dispatcher):
    # Enregistrement des commandes
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("update_openai_token", update_openai_token))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
