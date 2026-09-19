import os

from google import genai


class GeminiService:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise RuntimeError("GEMINI_API_KEY is not configured in .env")
        self.client = genai.Client(api_key=api_key)
        self.model = os.getenv("GEMINI_MODEL", "gemini-3.6-flash")

    def answer(self, question: str, context: str) -> str:
        prompt = f"""
You are a student database assistant.

Answer the user's question using the database context below.
Do not invent student records. If the context does not contain enough
information, clearly say that the requested information is not available.

Database context:
{context}

User question:
{question}

Give a concise, useful answer. When listing students, include relevant
fields such as name, department, semester and CGPA when available.
"""
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
        )
        return response.text or "I could not generate an answer."
