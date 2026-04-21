# -------------------- IMPORTS --------------------
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

# -------------------- LOAD ENV --------------------
load_dotenv()

# -------------------- MODEL --------------------
model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

# -------------------- PROMPT --------------------
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} in simple words"
)

# -------------------- PARSER --------------------
parser = StrOutputParser()

# -------------------- RUNNABLE LAMBDA (OUTPUT MODIFIER) --------------------
def modify_output(text):
    # modify LLM output
    return "FINAL ANSWER:\n" + text.upper()

output_lambda = RunnableLambda(modify_output)

# -------------------- CHAIN --------------------
chain = prompt | model | parser | output_lambda

# -------------------- RUN --------------------
response = chain.invoke({"topic": "Machine Learning"})
print(response)