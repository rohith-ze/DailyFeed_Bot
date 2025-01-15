import schedule
import time

def job():
    content = get_groq_content("Daily inspiration")
    post_to_reddit("test", "Daily Inspiration", content)

schedule.every().day.at("10:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
