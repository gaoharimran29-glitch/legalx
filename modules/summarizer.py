from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

def generate_summary(text):

    prompt = f"""
    You are a legal educator.

    Summarize the following legal document.

    Requirements:
    - Maximum 250 words
    - Easy language
    - Suitable for non-legal users
    - Explain purpose and importance
    - Only reply with info from legal document

    DOCUMENT:
    {text[:15000]}
    """

    response = model.invoke(prompt)

    return response.content