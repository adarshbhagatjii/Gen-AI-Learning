import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

# OpenRouter setup
llm = ChatOpenAI(

    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    model="deepseek/deepseek-chat" # You can choose any free model here
)

response = llm.invoke("Give one story")

print(response.content)