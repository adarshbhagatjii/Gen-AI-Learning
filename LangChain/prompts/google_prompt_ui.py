import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

# --------------------------------
# ENV SETUP
# --------------------------------
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("❌ GOOGLE_API_KEY not found. Please check your .env file")
    st.stop()

# --------------------------------
# GEMINI LLM (YOUR EXACT CONFIG)
# --------------------------------
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7,
    google_api_key=api_key
)

# --------------------------------
# STREAMLIT UI
# --------------------------------
st.set_page_config(page_title="Prompt Engineering Lab", layout="wide")
st.title(" Prompty AI 👻")
st.caption("Build powerful prompts using Role · Task · Constraints · Examples · Format")

# --------------------------------
# OPTIONS
# --------------------------------
roles = [
    "Senior Software Engineer",
    "Data Science Trainer",
    "Gen-Z Content Creator",
    "Socratic Teacher",
    "Startup Founder",
    "Stand-up Comedian",
    "Strict Code Reviewer",
    "AI Interviewer",
    "Bollywood Script Writer",
    "My brutally honest mentor"
]

tasks = [
    "Explain",
    "Rewrite",
    "Summarize",
    "Teach step-by-step",
    "Critically analyze",
    "Create interview questions on",
    "Simplify for beginners",
    "Convert into a story",
    "Make it funny",
    "Give real-world applications of"
]

constraints = [
    "Use simple English",
    "Avoid technical jargon",
    "Under 100 words",
    "Use bullet points",
    "Use emojis",
    "No emojis",
    "Explain like I am 10",
    "Add Indian context",
    "Be concise",
    "Be dramatic"
]

examples = [
    "No examples",
    "Provide 1 example",
    "Provide 2 real-world examples",
    "Provide analogy-based example",
    "Provide code example"
]

formats = [
    "Plain paragraph",
    "Bullet points",
    "Numbered steps",
    "Markdown table",
    "Q&A format",
    "Cheat-sheet style",
    "Interview-ready answer"
]

# --------------------------------
# UI LAYOUT
# --------------------------------
col1, col2 = st.columns(2)

with col1:
    role = st.selectbox("🎭 Role", roles)
    task = st.selectbox("🛠 Task", tasks)
    example_mode = st.selectbox("📚 Examples", examples)

with col2:
    output_format = st.selectbox("📤 Output Format", formats)
    selected_constraints = st.multiselect("⛓ Constraints", constraints)

content = st.text_area(
    "📌 Content / Topic",
    placeholder="Enter your topic or text here...",
    height=160
)

# --------------------------------
# PROMPT TEMPLATE
# --------------------------------
prompt = PromptTemplate.from_template(
"""
ROLE:
You are acting as {role}.

TASK:
Your task is to {task} the following content.

CONTENT:
{text}

CONSTRAINTS:
{constraints}

EXAMPLES:
{examples}

OUTPUT FORMAT:
{format}

RULES:
- Follow all constraints strictly
- Do not mention prompt structure
- Be clear, accurate, and engaging

FINAL ANSWER: 
"""
)
#completion anchor- Final answer

constraint_text = (
    "- " + "\n- ".join(selected_constraints)
    if selected_constraints else "No specific constraints"
)

# --------------------------------
# BUTTON
# --------------------------------
if st.button("🚀 Generate Output"):
    if not content.strip():
        st.warning("⚠️ Please enter some content")
    else:
        with st.spinner("👻 Prompty is thinking..."):
            try:
                response = llm.invoke(
                    prompt.format(
                        role=role,
                        task=task,
                        text=content,
                        constraints=constraint_text,
                        examples=example_mode,
                        format=output_format
                    )
                )

                st.markdown("## ✨ Prompty AI Output")
                st.write(response.content)

            except Exception as e:
                st.error(f"❌ Error: {e}")

# --------------------------------
# FOOTER
# --------------------------------
st.markdown("---")
st.caption("Built by Adarsh with ❤️ using LangChain + Gemini 2.5 Flash")