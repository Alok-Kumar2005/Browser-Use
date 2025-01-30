from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('GOOGLE_API_KEY')


async def main():
    agent = Agent(
        task = "Go to the Reddit, search fot 'browser-use in the search bar, click on the first post and return the first comment.",
        llm = ChatGoogleGenerativeAI(model = 'gemini-1.5-flash' , api_key=api_key),
    )
    result = await agent.run()
    print(result)

asyncio.run(main())