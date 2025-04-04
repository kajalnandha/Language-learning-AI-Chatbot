from openai import AsyncOpenAI

class LanguageLearningBot:
    def __init__(self, target_language: str):
        self.target_language = target_language
        self.conversation_history = []
        self.client = AsyncOpenAI()
        
    async def chat(self, user_message: str) -> str:
        try:
            # Add user message to history
            self.conversation_history.append({"role": "user", "content": user_message})
            
            # Create system message
            system_message = {
                "role": "system",
                "content": f"You are a helpful language learning assistant for {self.target_language}. "
                          f"Help users learn through conversation, correct their mistakes gently, "
                          f"and provide translations when needed."
            }
            
            # Get response from OpenAI
            response = await self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[system_message] + self.conversation_history,
                temperature=0.7
            )
            
            bot_response = response.choices[0].message.content
            self.conversation_history.append({"role": "assistant", "content": bot_response})
            
            return bot_response
            
        except Exception as e:
            return f"Sorry, I encountered an error: {str(e)}"