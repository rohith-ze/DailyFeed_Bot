import praw
import os
from dotenv import load_dotenv

#Load .env file for credentials
load_dotenv(dotenv_path="/media/rohith/15905E2C2B6C1D69/vscode/Github_repos/DailyFeed_Bot/key.env")

reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    username=os.getenv("USERNAME"),
    password=os.getenv("PASSWORD"),
    user_agent=os.getenv("USER_AGENT")
)
