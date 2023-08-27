import openai
from src.utils import helpers  # Assurez-vous que le chemin d'importation est correct

class ChatModel:
    def __init__(self, api_key, model="text-davinci-002"):
        self.api_key = api_key
        self.model = model
        openai.api_key = self.api_key

    def get_response(self, prompt):
        # Nettoie l'entrée utilisateur
        prompt = helpers.sanitize_user_input(prompt)

        # Enregistrement du message d'envoi à l'API dans la console
        helpers.log_message(f"Envoi de la requête à l'API OpenAI avec le prompt : {prompt}")

        response = openai.Completion.create(
            engine=self.model,
            prompt=prompt,
            max_tokens=50  # Vous pouvez ajuster ce nombre selon vos besoins
        )

        # Enregistrement du message de réponse de l'API dans la console
        helpers.log_message(f"Réponse reçue de l'API OpenAI : {response.choices[0].text.strip()}")

        return response.choices[0].text.strip()

# Exemple d'utilisation
if __name__ == "__main__":
    api_key = "votre_clé_API_OpenAI"
    chat_model = ChatModel(api_key)
    print(chat_model.get_response("Bonjour, comment vas-tu ?"))
