import requests
import os
from dotenv import load_dotenv

#Load .env file for credentials
load_dotenv(dotenv_path="/media/rohith/15905E2C2B6C1D69/vscode/Github_repos/DailyFeed_Bot/key.env")


def get_groq_content(prompt):
    url = "https://api.groq.ai/v1/generate"
    headers = {"Authorization": os.getenv("GROQAPI")}
    data = {"prompt": prompt}
    
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        return response.json().get("content")
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")

