import logging

logging.basicConfig(filename="bot.log", level=logging.INFO)

try:
    job()
    logging.info("Post successful")
except Exception as e:
    logging.error(f"Error occurred: {e}")
