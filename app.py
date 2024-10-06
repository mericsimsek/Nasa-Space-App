from transformers import pipeline
from fastapi import FastAPI, Request
import uvicorn

# Summarizer modelini yükleyin
summarizer = pipeline("summarization", model="t5-small")

# FastAPI instance oluşturun
app = FastAPI()

@app.post("/summarize")
async def summarize(request: Request):
    data = await request.json()
    text = data.get("text")
    if not text:
        return {"error": "No text provided"}
    # Metni özetleyin
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)[0]['generated_text']
    return {"summary": summary}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
