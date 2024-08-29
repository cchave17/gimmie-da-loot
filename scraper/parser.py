from bs4 import BeautifulSoup

def extract_article_links(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract article links based on the structure you provided
    article_links = []
    for entry in soup.find_all('div', class_='wpex-post-cards-entry'):
        title_tag = entry.find('h2', class_='wpex-card-title')
        link = title_tag.find('a')['href']
        article_links.append(link)
    
    return article_links

def extract_articles_from_main_page(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    articles = []

    for entry in soup.find_all('div', class_='wpex-post-cards-entry'):
        title_tag = entry.find('h2', class_='wpex-card-title')
        title = title_tag.get_text(strip=True)
        link = title_tag.find('a')['href']
        
        excerpt_tag = entry.find('div', class_='wpex-card-excerpt')
        description = excerpt_tag.get_text(strip=True) if excerpt_tag else None

        articles.append({
            'title': title,
            'article_link': link,
            'description': description,
        })

    return articles

def parse_article(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract metadata like title, author, excerpt, etc.
    title_tag = soup.find('h2', class_='wpex-card-title')
    title = title_tag.get_text(strip=True) if title_tag else None
    
    author_tag = soup.find('div', class_='spauthor') or soup.find('div', class_='spguestname')
    author = author_tag.get_text(strip=True) if author_tag else None
    
    excerpt_tag = soup.find('div', class_='spexcerpt')
    excerpt = excerpt_tag.get_text(strip=True) if excerpt_tag else None
    
    category_tag = soup.find('div', class_='article-category')
    category = category_tag.get_text(strip=True) if category_tag else None
    
    image_tag = soup.find('div', class_='wpex-card-thumbnail').find('img')
    image_url = image_tag['src'] if image_tag else None
    
    metadata_tag = soup.find('div', class_='sppodcastmeta')
    metadata = metadata_tag.get_text(strip=True) if metadata_tag else None
    
    # Return the extracted metadata
    return {
        'title': title,
        'author': author,
        'excerpt': excerpt,
        'category': category,
        'image_url': image_url,
        'metadata': metadata
    }

