# -------------------- IMPORTS --------------------
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

# -------------------- LOAD ENV --------------------
load_dotenv()

# -------------------- MODEL --------------------
model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

# -------------------- OUTPUT PARSER --------------------
parser = StrOutputParser()

# -------------------- PROMPT 1: SUMMARY --------------------
summary_prompt = PromptTemplate(
    input_variables=["topic"],
    template="Give a short summary of {topic}"
)

summary_chain = summary_prompt | model | parser

# -------------------- PROMPT 2: ADVANTAGES --------------------
adv_prompt = PromptTemplate(
    input_variables=["topic"],
    template="What are the advantages of {topic}?"
)

adv_chain = adv_prompt | model | parser

# -------------------- PROMPT 3: DISADVANTAGES --------------------
dis_prompt = PromptTemplate(
    input_variables=["topic"],
    template="What are the disadvantages of {topic}?"
)

dis_chain = dis_prompt | model | parser

# -------------------- RUNNABLE PARALLEL --------------------
parallel_chain = RunnableParallel(
    summary=summary_chain,
    advantages=adv_chain,
    disadvantages=dis_chain
)

# -------------------- INVOKE --------------------
response = parallel_chain.invoke({"topic": "Artificial Intelligence"})

# -------------------- OUTPUT --------------------
print("\nSUMMARY:\n", response["summary"])
print("\nADVANTAGES:\n", response["advantages"])
print("\nDISADVANTAGES:\n", response["disadvantages"])
 

