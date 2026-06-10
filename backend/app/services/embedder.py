import os
import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)


class GeminiEmbedder:

    def generate_embedding(self, text):

        response = genai.embed_content(
            model="models/embedding-001",
            content=text
        )

        return response["embedding"]