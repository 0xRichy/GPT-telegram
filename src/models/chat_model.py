import openai

class ChatModel:
    def __init__(self, api_key, model="text-davinci-002"):
        self.api_key = api_key
        self.model = model
        openai.api_key = self.api_key

    def get_response(self, prompt):
        response = openai.Completion.create(
            engine=self.model,
            prompt=prompt,
            max_tokens=50  # Vous pouvez ajuster ce nombre selon vos besoins
        )
        return response.choices[0].text.strip()

# Exemple d'utilisation
if __name__ == "__main__":
    api_key = "votre_clé_API_OpenAI"
    chat_model = ChatModel(api_key)
    print(chat_model.get_response("Bonjour, comment vas-tu ?"))
