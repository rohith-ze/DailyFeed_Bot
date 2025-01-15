def post_to_reddit(subreddit, title, content):
    subreddit_instance = reddit.subreddit(subreddit)
    subreddit_instance.submit(title=title, selftext=content)
