import asyncio
import os
from dotenv import load_dotenv
from src.chatbot import LanguageLearningBot

async def main():
    load_dotenv()
    
    # Initialize OpenAI API key
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    # Create chatbot instance
    bot = LanguageLearningBot("Spanish")  # You can change the target language
    
    print("Language Learning Chatbot (type 'quit' to exit)")
    print("----------------------------------------------")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'quit':
            break
            
        response = await bot.chat(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    asyncio.run(main())