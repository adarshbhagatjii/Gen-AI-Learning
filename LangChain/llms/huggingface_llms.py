import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.messages import HumanMessage

load_dotenv()

# Using Zephyr-7b-beta because it natively supports the 'conversational' task 
# required by ChatHuggingFace, avoiding the 'Mistral v0.3' task errors.

# 1. Setup the endpoint
model = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    max_new_tokens=512,
    temperature=0.7,
)

# 2. Wrap in ChatHuggingFace
chat_model = ChatHuggingFace(llm=model)

# 3. Execution
response = chat_model.invoke([HumanMessage(content="Create a story of Cat")])

print(response.content)