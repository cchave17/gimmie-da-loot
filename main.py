from scraper.scraper import fetch_main_page, fetch_article_page
from scraper.parser import extract_article_links, parse_article
from scraper.utils import create_article_directory, save_metadata
from logs.log import get_logger

logger = get_logger(__name__)

if __name__ == "__main__":
    main_page_html = fetch_main_page()
    article_links = extract_article_links(main_page_html)

    base_dir = 'data/scraped_articles'

    for i, article_url in enumerate(article_links):
        article_html = fetch_article_page(article_url)
        metadata = parse_article(article_html)

        # Create article directory and save metadata
        folder_path = create_article_directory(base_dir, metadata['title'], i + 1)
        save_metadata(folder_path, metadata)

        # Log the directory creation
        logger.info(f"Created directory and saved metadata for: {metadata['title']}")
