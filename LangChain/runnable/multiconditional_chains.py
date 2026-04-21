from dotenv import load_dotenv
import os

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=os.getenv("GROQ_API_KEY")
)

parser = StrOutputParser()

# -------- chains --------
python_chain = PromptTemplate.from_template(
    "Explain {topic} as programming language"
) | llm | parser

ai_chain = PromptTemplate.from_template(
    "Explain {topic} in AI field"
) | llm | parser

math_chain = PromptTemplate.from_template(
    "Explain {topic} as maths concept"
) | llm | parser

general_chain = PromptTemplate.from_template(
    "Explain {topic} in general"
) | llm | parser

# ==================================================
# 🔷 Multiple condition branch
# ==================================================
branch = RunnableBranch(
    (lambda x: x["topic"].lower() == "python", python_chain),
    (lambda x: x["topic"].lower() == "ai", ai_chain),
    (lambda x: x["topic"].lower() == "maths", math_chain),
    general_chain   # default (else)
)

# ---------------- RUN ----------------
print(branch.invoke({"topic": "python"}))
print(branch.invoke({"topic": "AI"}))
print(branch.invoke({"topic": "maths"}))
print(branch.invoke({"topic": "tree"}))
 


