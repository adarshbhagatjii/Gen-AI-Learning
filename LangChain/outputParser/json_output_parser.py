from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

parser = JsonOutputParser()

template = PromptTemplate(
    input_variables=["movie"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
    template="""
Give movie details in JSON format.

Movie: {movie}

{format_instructions}

JSON should contain:
title, director, year, description
"""
)

chain = template | model | parser

response = chain.invoke({"movie": "Inception"})
print(response)
print(response["title"])