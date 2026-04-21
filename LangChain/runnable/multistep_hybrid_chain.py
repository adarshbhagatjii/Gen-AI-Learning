'''topic → explanation  
      → summary  
      → interview question  
      → final report combine
'''
# -------------------- IMPORTS --------------------
from dotenv import load_dotenv
import os

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableLambda

# -------------------- LOAD ENV --------------------
load_dotenv()

# -------------------- MODEL --------------------
model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

parser = StrOutputParser()

# -------------------- STEP 1: EXPLANATION --------------------
explain_prompt = PromptTemplate.from_template(
    "Explain {topic} in simple words"
)

explain_chain = explain_prompt | model | parser

# -------------------- STEP 2: PARALLEL TASKS --------------------
summary_prompt = PromptTemplate.from_template(
    "Summarize this text in 2 lines: {text}"
)

question_prompt = PromptTemplate.from_template(
    "Create 1 interview question from this text: {text}"
)

summary_chain = summary_prompt | model | parser
question_chain = question_prompt | model | parser

parallel_chain = RunnableParallel(
    summary = summary_chain,
    interview_question = question_chain
)

# -------------------- STEP 3: COMBINE OUTPUT --------------------
def combine_output(data):
    return f"""
FULL REPORT

Explanation:
{data['summary']}

Interview Question:
{data['interview_question']}
"""

combine_chain = RunnableLambda(combine_output)

# -------------------- FINAL HYBRID CHAIN --------------------
final_chain = (
    explain_chain
    | RunnableLambda(lambda x: {"text": x})
    | parallel_chain
    | combine_chain
)

# -------------------- INVOKE --------------------
result = final_chain.invoke({
    "topic": "Machine Learning"
})

print(result)
 


