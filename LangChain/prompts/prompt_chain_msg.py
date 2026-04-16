# This program gives some information to the AI, asks a question,
# and the AI answers only from that information.

# Load environment variables (like API keys) from .env file
from dotenv import load_dotenv
import os

# Import Groq chat model, prompt template and message classes
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

# Initialize the Groq chat model
model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.0,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

# Define reusable prompt template
template = PromptTemplate.from_template(
    """You are a helpful assistant that answers questions based on the provided context.
If you can't find the answer in the context, say 'I don't know'.
Context: {context}
Question: {question}
Answer:"""
)

# Provide actual context and question
user_input = {
    "context": "The capital of India is New Delhi. It is the seat of the government of India and is known for its rich history and cultural heritage.",
    "question": "What is the capital of France?"
}

# -----------------------------
# Create chain (Prompt → Model)
# -----------------------------
chain = template | model

# Format prompt using template
formatted_prompt = template.format(**user_input)

# Create system + human messages
messages = [
    SystemMessage(content="You are a helpful AI assistant."),
    HumanMessage(content=formatted_prompt)
]

# Invoke model using chain concept
response = model.invoke(messages)

print("--------------------------------")
print(response.content)