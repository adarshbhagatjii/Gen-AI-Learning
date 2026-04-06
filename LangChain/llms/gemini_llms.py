import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# 1. Load your .env file
load_dotenv()

# 2. Grab the API Key from the environment
api_key = os.getenv("GOOGLE_API_KEY")


 # 3. Initialize Gemini LLM
# Using gemini-2.5-flash: Best balance of speed and free-tier quota
llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash", 
        temperature=0.7,
        google_api_key=api_key
    )

response = llm.invoke("What is the capital of India?")
        
# 5. Print only the text part of the response

print(response.content)