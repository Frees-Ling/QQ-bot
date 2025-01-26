from wit import Wit
import os
from dotenv import load_dotenv

load_dotenv(".env")

wit_client = Wit(os.getenv("WIT_AI_API_KEY"))

def chat_answer(text):
    response = wit_client.message(text)
    return response['text']