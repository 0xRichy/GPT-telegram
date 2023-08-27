# Initialisation du token OpenAI
OPENAI_API_TOKEN = "Votre_Token_API_OpenAI"

# Initialisation du token Telegram
TELEGRAM_API_TOKEN = "Votre_Token_API_Telegram"

# Initialisation du Chat ID Telegram
TELEGRAM_CHAT_ID = "Votre_Chat_ID_Telegram"

def update_openai_api_token(new_token):
    global OPENAI_API_TOKEN
    OPENAI_API_TOKEN = new_token
