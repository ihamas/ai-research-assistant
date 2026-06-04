from fastapi import FastAPI
from pydantic import BaseModel
from graph import research_app


app = FastAPI()

class ResearchRequest(BaseModel):
    question: str

@app.post("/ask")
def ask(request: ResearchRequest):
    answer = research_app.invoke({"question": request.question, "iterations": 0})    
    return answer["answer"]

