import requests
from config.settings import BASE_URL, HEADERS
from logs.log import get_logger

logger = get_logger(__name__)

def fetch_main_page():
    try:
        response = requests.get(BASE_URL, headers=HEADERS)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching main page: {e}")
        raise

def fetch_article_page(url):
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching article page {url}: {e}")
        raise
