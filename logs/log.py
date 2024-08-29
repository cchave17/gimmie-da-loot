import logging

# Configure the logger
logging.basicConfig(
    filename='logs/scraper.log',
    filemode='a',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Function to get the logger instance
def get_logger(name):
    return logging.getLogger(name)
