import os
from dotenv import load_dotenv

load_dotenv()

def load_mantium_env() -> tuple:
    mantium_user = os.getenv('MANTIUM_USER')
    mantium_password = os.getenv('MANTIUM_PASSWORD')
    prompt_id = os.getenv('PROMPT_ID')

    return mantium_user, mantium_password, prompt_id