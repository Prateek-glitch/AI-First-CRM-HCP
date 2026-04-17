import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

GROQ_MODEL = os.getenv("GROQ_MODEL", "gemma2-9b-it")

def summarize_interaction_with_llm(payload: dict) -> str:
    llm = ChatGroq(model=GROQ_MODEL, temperature=0.2)

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a pharma CRM assistant. Summarize interaction in 2-3 concise lines."),
        ("human",
         "Interaction Type: {interaction_type}\n"
         "Date: {interaction_date}\n"
         "Attendees: {attendees}\n"
         "Topics: {topics_discussed}\n"
         "Return a professional concise summary.")
    ])

    chain = prompt | llm
    resp = chain.invoke(payload)
    return resp.content.strip()