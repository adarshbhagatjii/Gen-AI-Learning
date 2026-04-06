import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# 1. Load keys
load_dotenv()

# 2. Initialize Groq LLM
# llama-3.3-70b-versatile is currently the best "all-rounder" on Groq
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.5,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

# 3. Test it

response = llm.invoke("Create a poem")
print("Groq Response:")
print(response.content)