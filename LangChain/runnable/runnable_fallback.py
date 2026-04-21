from dotenv import load_dotenv
import os

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# ---------------- MAIN LLM ----------------
main_llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

# ---------------- BACKUP LLM ----------------
backup_llm = ChatGroq(
    model="llama3-8b-8192",   # lighter model as backup
    temperature=0.5,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

parser = StrOutputParser()

# ---------------- PROMPT ----------------
prompt = PromptTemplate.from_template(
    "Explain {topic} in simple words"
)

# ---------------- CHAINS ----------------
main_chain = prompt | main_llm | parser
backup_chain = prompt | backup_llm | parser

# ===================================================
# 🔷 ADD FALLBACK
# ===================================================
safe_chain = main_chain.with_fallbacks([backup_chain])

# ---------------- RUN ----------------
result = safe_chain.invoke({"topic": "Artificial Intelligence"})

print(result)
 


