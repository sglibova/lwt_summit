# Sentiment Analysis with Mantium, Python, and roBERTa

## Getting Started with Mantium
Welcome and thank you for joining the Mantium team for our upcoming workshop! To prepare you for participating, we have included a few steps below to help you get set up for success.

### 1. Create a Mantium Account and get a Provider API Key

*Note: To participate in this demo, you are only required to have a Mantium account username, password, and prompt_id for a roBERTa prompt.*

For creating other prompts, you will need a Mantium account and an API key for an LLM (large language model) provider - this short [Loom video](https://www.loom.com/share/cb6136ebe0694c34a3c72c3f2651678f) will take you through the process. If you do not wish to use a non-Mantium LLM provider, you are welcome to use Mantium GPT-J without an API key!

### 2. Join our Discord Community!

Join our [Discord server](https://discord.com/invite/h9NCwW6mXY) and share your ideas, teach, and learn about the world of growing AI technologies. New to coding? No problem. This is an inclusive space!

### 3. Try Out a Mantium Prompt

To get an understanding of the type of application you will be building in the workshop, we’ve included a link to an interactive demo prompt. This is the [Mantium Video Game Generator](https://share.mantiumai.com/prompt/284001e2-1345-4df9-909a-9c5ba95001c7) - all you have to do is type in a creative video game title for a game that might not yet exist, and the language model will generate a unique description! Try it out as many times as you’d like, and feel free to share any fun responses with us.

The [Mantium developer hub](https://developer.mantiumai.com/) can be found here. If you’d like to learn more, this is where you’ll find tutorials and documentation!

### 4. Prepare Sentiment Analysis 

To build your own sentiment analysis prompt, create one in the Mantium UI.

Step 1: Navigate to `AI Manager > Prompts`

Step 2: Click `Add new prompt`

Step 3: Choose `Mantium` as a Provider and `Roberta_Base_Goemotions_Classification` as the endpoint.

Step 4: Fill in the `Name of Prompt` and click `Save`

Step 5: To locate the `prompt_id` value (used in the next step), select your prompt from the `Prompts` menu and copy the hash value found in the Endpoint API property.

## CONFIGURE ENVIRONMENT VARIABLES
Reminder: please never use unencrypted environment variables in production, and never push them to a public repo!

Step 1: Update `.env-demo` to `.env`

`$ mv .env-demo .env`

Step 2: Replace placeholder strings in `.env` with your Mantium credentials


## DEMO SETUP USING PYENV VIRTUALENV + VIRTUALENVWRAPPER
Step 1: Change into a directory where you keep your projects

`$ cd ~/path/to/your/projects`

Step 2: Clone this repository into your projects directory

`$ git clone url/to/this/repository`

Step 3: Change into the directory where you cloned the repository

`$ cd ~/path/to/your/projects/lwt_summit`

Step 4: Create a virtual environment

`$ mkvirtualenv mantium_python_project`

Step 7: Install the project dependencies using pip

`$ pip install -r requirements.txt`

If you use other methods, feel free to adapt these steps to your needs!

## RUN BACKEND AND SEND REQUESTS VIA OPENAPI INTERACTIVE DOCUMENTATION

With `FastAPI` and `Uvicorn` you should be able to run the backend with one simple command:

`$ uvicorn main:app --reload`

To send requests:

Step 1: Navigate to `http://127.0.0.1:8000/docs` in your browser 

Step 2: Expand the `POST` route by clicking the dropdown arrow on the right and click `Try it out`

Step 3: Modify the value of `"input"` with a string that you'd like to have analyzed and click `Execute`!
