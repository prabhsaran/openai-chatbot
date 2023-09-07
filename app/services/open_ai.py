import os
import openai


class OpenAIService:

    def __init__(self):
        openai.api_key = os.getenv('OPEN_AI_API_KEY')
        self.completion = openai.ChatCompletion()

    def query(self, question: str, chat_log: str = None):
        """Query OpenAI API"""

        messages = [{"role": "user", "content": question}]

        response = self.completion.create(model="gpt-4", messages=messages)
        response_message = response["choices"][0]["message"]['content']
        return response_message
