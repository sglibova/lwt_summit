from analyze_text import analyze_sentiment
from schemas import Input, Output
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello from Sentiment Analysis! We will use the Mantium Client and RoBERTa model to analyze the sentiment of your text."}

@app.post("/analyze/")
async def return_analysis(input_text: Input) -> Output:
    input_output_dict = input_text.dict()
    output = analyze_sentiment(input_text)
    input_output_dict.update({"output": output})
    return input_output_dict
