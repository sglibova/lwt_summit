"""Main Module for FastAPI Mantium Application for Sentiment Analysis."""
from analyze_text import analyze_sentiment
from schemas import Input, Output
from fastapi import FastAPI

import logging


logging.basicConfig(level=logging.INFO)
app = FastAPI()

@app.get("/")
async def root():
    """Root endpoint for the FastAPI Mantium application."""
    return {"message": "Hello from Sentiment Analysis! We will use the Mantium Client and RoBERTa model to analyze the sentiment of your text."}

@app.post("/analyze/")
async def return_analysis(input_text: Input) -> Output:
    """Sentinment analysis endpoint for the FastAPI Mantium application."""
    logging.info(f"received input text: {input_text}")
    input_output_dict = input_text.dict()
    try:
        output = analyze_sentiment(input_text)
        logging.info(f"sentiment analysis complete: {output}")
        input_output_dict.update({"output": output})
        return input_output_dict
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"error": str(e)}
