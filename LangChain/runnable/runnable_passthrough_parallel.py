from dotenv import load_dotenv
import os

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableParallel

load_dotenv()

# ---------------- LLM ----------------
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

parser = StrOutputParser()

# ---------------- PROMPT 1 (Explain) ----------------
explain_prompt = PromptTemplate.from_template(
    "Explain {topic} in simple words"
)

explain_chain = explain_prompt | llm | parser

# ---------------- PROMPT 2 (Joke) ----------------
joke_prompt = PromptTemplate.from_template(
    "Tell one funny joke about {topic}"
)

joke_chain = joke_prompt | llm | parser

# =========================================================
# 🔷 RunnablePassthrough at beginning
# It sends SAME input to both chains
# =========================================================
start = RunnablePassthrough()

# =========================================================
# 🔷 Parallel: two different tasks with same input
# =========================================================
final_chain = start | RunnableParallel(
    explanation = explain_chain,
    joke = joke_chain
)

# ---------------- RUN ----------------
result = final_chain.invoke({
    "topic": "Python"
})

print("\nFINAL RESULT:\n")
print(result)
 

