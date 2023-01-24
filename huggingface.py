from fastapi import FastAPI, Depends, HTTPException, Body
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.on_event("startup")
async def load_models():
    try:
        app.model = AutoModelForSeq2SeqLM.from_pretrained('yjernite/bart_eli5')
        app.tokenizer = AutoTokenizer.from_pretrained('yjernite/bart_eli5')
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading the model: {e}")

def get_context(context: str = None):
    if context is None:
        raise HTTPException(status_code=400, detail="Context is required")	
    try:
        page = requests.get(context)
        soup = BeautifulSoup(page.content, 'html.parser')
        text = soup.get_text()
        return text[:4096]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error parsing the url {context}")
    return context

@app.post("/answer")
async def generate_answer(prompt: str, context: str = None):
    try:
        if context.startswith("http"):
            context = get_context(context)
        inputs = app.tokenizer.encode(prompt, context, max_length=4096, return_tensors='pt')
        outputs = app.model.generate(inputs, max_length=4096)
        return app.tokenizer.decode(outputs[0], skip_special_tokens=True)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating the answer: {e}")

@app.get("/")
async def root():
    return {"message": "Welcome to the QA API"}

