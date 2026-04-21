'''Idea:

If topic = python → beginner explanation
Else → advanced explanation'''
# -------------------- IMPORTS --------------------
from dotenv import load_dotenv
import os

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch

# -------------------- LOAD ENV --------------------
load_dotenv()

# -------------------- MODEL --------------------
model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

parser = StrOutputParser()

# -------------------- PROMPTS --------------------
beginner_prompt = PromptTemplate.from_template(
    "Explain {topic} for a 10 year old beginner"
)

advanced_prompt = PromptTemplate.from_template(
    "Explain {topic} in technical depth for engineers"
)

# chains
beginner_chain = beginner_prompt | model | parser
advanced_chain = advanced_prompt | model | parser

# -------------------- CONDITIONAL BRANCH --------------------
# if topic == python → beginner
# else → advanced

conditional_chain = RunnableBranch(
    (lambda x: x["topic"].lower() == "python", beginner_chain),
    advanced_chain
)

# -------------------- INVOKE --------------------
result = conditional_chain.invoke({
    "topic": "Python"
})

print("\nFINAL ANSWER:\n")
print(result)