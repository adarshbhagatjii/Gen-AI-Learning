from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# ---------------- LLM ----------------
model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

# ---------------- STRING parser ----------------
parser = StrOutputParser()

# ---------------- Prompt ----------------
template = PromptTemplate(
    input_variables=["movie"],
    template="""
Give complete details of the movie in simple text format.

Movie: {movie}

Include:
- title
- director
- year
- short description
"""
)

# ---------------- Chain ----------------
chain = template | model | parser

# ---------------- Invoke ----------------
response = chain.invoke({"movie": "Mission Mangal"})

# ---------------- Output ----------------
print(response)