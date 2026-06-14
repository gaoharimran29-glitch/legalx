from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0)

class ExtractedInfo(BaseModel):
    rights: list[str] = Field(description="Key rights mentioned in the legal document")
    provisions: list[str] = Field(description="Important provisions of the legal document")
    penalties: list[str] = Field(description="Important penalties mentioned in the legal document")
    beneficiaries: list[str] = Field(description="Who benefits from this law")

structured_model = model.with_structured_output(ExtractedInfo)

def extract_information(text):

    try:

        prompt = f"""
            You are a legal analyst.

            Analyze the legal document.

            Extract:

            - 5-10 key rights
            - 5-10 important provisions
            - 5-10 penalties
            - 5-10 beneficiaries

            Keep entries short and user-friendly.

            Document:
            {text[:15000]}
            """

        response = structured_model.invoke(prompt)

        return response.model_dump()

    except Exception as e:

        print("Extraction Error:", e)

        return {
            "rights": [],
            "provisions": [],
            "penalties": [],
            "beneficiaries": []
        }