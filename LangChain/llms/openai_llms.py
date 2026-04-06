from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model="gpt-3.5-turbo",temperature=0.0,max_tokens=1000)

response=llm.invoke("When is the republic day celebrated in India?")

print(response.content) 