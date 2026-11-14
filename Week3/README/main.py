# main.py
import os

from dotenv import load_dotenv

from llm_client import GeminiProvider, OllamaProvider, LLMClient
from mongo_logger import MongoLogger


def main():
    load_dotenv(override=True)

    print("================================")
    print("       WEEK 3: LLM MONITORING")
    print("================================")
    print("1. Gemini")
    print("2. Ollama")

    choice = input("\nSelect provider (1/2): ").strip()
    logger = None

    try:
        logger = MongoLogger()
        print("Connected to MongoDB successfully!")

        if choice == "1":
            api_key = os.getenv("GEMINI_API_KEY", "").strip()
            if not api_key or api_key == "YOUR_GEMINI_API_KEY":
                raise ValueError(
                    "Gemini API key missing. Add it to the .env file."
                )
            model = os.getenv("GEMINI_MODEL", "gemini-3-flash-pro").strip()
            provider = GeminiProvider(api_key, model)

        elif choice == "2":
            provider = OllamaProvider("llama3.2")

        else:
            raise ValueError("Invalid selection. Choose 1 or 2.")

        client = LLMClient(provider, logger)
        prompt = input("\nEnter your question: ").strip()

        if not prompt:
            raise ValueError("Please enter a question.")

        answer = client.generate(prompt)

        print("\n========== AI RESPONSE ==========")
        print(answer)
        print("\n========== COMPLETED ==========")

    except Exception as error:
        print("\nApplication error:", error)

    finally:
        if logger is not None:
            logger.close()


if __name__ == "__main__":
    main()
