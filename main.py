import praw
import os
from dotenv import load_dotenv

#Load .env file for credentials
load_dotenv(dotenv_path="/media/rohith/15905E2C2B6C1D69/vscode/Github_repos/DailyFeed_Bot/key.env")

# Reddit API credentials from the environment variables
reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    username=os.getenv("USERNAME"),
    password=os.getenv("PASSWORD"),
    user_agent=os.getenv("USER_AGENT")
)

try:
    print("Authenticated as:", reddit.user.me())
except Exception as e:
    print("Error during authentication:", e)

#Fetch and print 5 posts from subreddit
subreddit = reddit.subreddit("Python")
for post in subreddit.hot(limit=5):
    print(post.title)
