import json
import logging
import time
import re
from utils import load_mantium_env
from schemas import Input

# load Mantium credentials
mantium_user, mantium_password, prompt_id = load_mantium_env()

from mantiumapi import prompt
from mantiumapi import client


logging.basicConfig(level=logging.INFO)

# Obtain bearer token and confirm log-in success
mantium_token = client.BearerAuth().get_token()
if mantium_token:
    logging.info(f"Mantium Login Successful with User {mantium_user}")

# Retrieve prompt by ID from Mantium
prompt = prompt.Prompt.from_id(prompt_id)

def clean_input(input: str) -> str:
    """ Cleans the input text to remove unnecessary spaces and line breaks.
    """

    # remove white space
    input = input.strip()
    # remove new line
    input = input.replace("\n", " ")
    # remove carriage return
    input = input.replace("\r", " ")
    # remove tabs
    input = input.replace("\t", " ")
    # remove multiple spaces
    input = re.sub(' +', ' ', input)

    return input

def parse_output(output: str) -> dict:
    """ Parse the output from the prompt and return an ordered dictionary.

    Args:
        output (str): Output from the sentiment analysis.

    Returns:
        dict: Ordered dictionary of the output. Top five results based on highest confidence score.
    """
    # convert output to a dict from the "emotions" key
    output_dict = json.loads(output)
    emotions = output_dict.get("response").get("outputs")[0].get("emotions")

    # return the top 5 results sorted by confidence score
    sorted_emotions = sorted(emotions, key=lambda k: k['score'], reverse=True)[:5]
    logging.info("Sorted Emotions: ", sorted_emotions)
    
    return sorted_emotions

def analyze_sentiment(input_text: Input) -> dict:
    """
    Retrieve results from the prompt above - uses a pre-configured prompt from ID.
    """
    cleaned_input = clean_input(input_text.input)

    executed_prompt = prompt.execute(f"{cleaned_input}")
    executed_prompt.refresh()

    time.sleep(5)  # prompt execution takes a small amount of time > this ensures a response
    executed_prompt.refresh()

    prompt_result = parse_output(executed_prompt.output)

	# check that the result is not an empty value and re-run the prompt if it is
    while prompt_result == "" or prompt_result=="{}":
        logging.info("Prompt Result Empty. Re-running prompt.")
        executed_prompt = prompt.execute(f"{input_text}")
        executed_prompt.refresh()

        time.sleep(5)  # prompt execution takes a small amount of time > this ensures a response
        prompt.refresh()

        prompt_result = parse_output(executed_prompt.output)

    return prompt_result

if __name__ == "__main__":
    result = analyze_sentiment("I have had a fabulous time in London. Please send mother my regards.")

    logging.info("The sentiments of this statement are: ", result)
    