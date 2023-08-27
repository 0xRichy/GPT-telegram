from telegram.ext import CommandHandler

def start(update, context):
    update.message.reply_text("Bonjour ! Je suis votre chatbot GPT-Telegram.")

def help_command(update, context):
    update.message.reply_text("Voici les commandes que vous pouvez utiliser:\n/start - Pour démarrer le bot\n/help - Pour obtenir de l'aide")

def custom_command(update, context):
    update.message.reply_text("Ceci est une commande personnalisée.")

def register_commands(dispatcher):
    # Enregistrement des commandes
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("custom", custom_command))
