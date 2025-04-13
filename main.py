from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import cohere

# Load .env file
load_dotenv()
COHERE_API_KEY = os.getenv("VRKOqhfKyTEfs9gzYfGBbnuIhO2qNNwiOsT1URJA")

# Initialize Cohere client
co = cohere.Client(COHERE_API_KEY)

app = FastAPI()

class CodeRequest(BaseModel):
    language: str
    code: str

@app.post("/fix-code")
async def fix_code(request: CodeRequest):
    prompt = f"Fix this {request.language} code and return only the corrected version:\n\n{request.code}"

    try:
        response = co.chat(
            message=prompt,
            model="command-nightly"
        )
        return {"fixed_code": response.text.strip()}  # ✅ Correct way for chat response
    except Exception as e:
        return {"error": str(e)}
