import openai
from src.config import settings  # Assurez-vous que le chemin d'importation est correct
from src.utils import helpers  # Assurez-vous que le chemin d'importation est correct

class ChatModel:
    def __init__(self):
        if settings.OPENAI_API_TOKEN is None:
            raise Exception("Veuillez configurer le token de l'API OpenAI.")
        self.api_key = settings.OPENAI_API_TOKEN
        openai.api_key = self.api_key

    def get_response(self, prompt):
        # Nettoie l'entrée utilisateur
        prompt = helpers.sanitize_user_input(prompt)

        # Enregistrement du message d'envoi à l'API dans la console
        helpers.log_message(f"Envoi de la requête à l'API OpenAI avec le prompt : {prompt}")

        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=50  # Vous pouvez ajuster ce nombre selon vos besoins
        )

        # Enregistrement du message de réponse de l'API dans la console
        helpers.log_message(f"Réponse reçue de l'API OpenAI : {response.choices[0].text.strip()}")

        return response.choices[0].text.strip()
