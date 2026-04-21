from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=os.getenv("GROQ_API_KEY")
)

prompt = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} simply"
)

parser = StrOutputParser()

# RunnableSequence using pipe
chain = prompt | model | parser

print(chain.invoke({"topic":"AI"}))