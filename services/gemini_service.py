from google import genai
from google.genai.types import GenerateContentConfig
from core.logger import setup_logger
from prompts.career_prompt import SYSTEM_PROMPT

logger = setup_logger()

class GeminiService:

    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)

    def generate_response(self, message, history):

        try:
            formatted_history = [
                f"{msg['role']}: {msg['content']}"
                for msg in history
            ]

            full_prompt = "\n".join(formatted_history) + f"\nuser: {message}"

            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=full_prompt,
                config=GenerateContentConfig(
                    system_instruction=SYSTEM_PROMPT,
                    temperature=0.5,
                    max_output_tokens=500
                )
            )

            logger.info("Gemini API call successful")
            return response.text

        except Exception as e:
            logger.error(f"Gemini API Error: {str(e)}")
            return "System temporarily unavailable. Please try again."
