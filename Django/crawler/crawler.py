import requests
from bs4 import BeautifulSoup

def fetch_and_parse(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.title.string.strip() if soup.title else "No title"

        # Extract books if from books.toscrape.com
        books = []
        if 'books.toscrape.com' in url:
            for book in soup.select('article.product_pod h3 a'):
                books.append(book['title'])

        return {
            "url": url,
            "title": title,
            "books": books
        }
    except Exception as e:
        return {
            "url": url,
            "title": f"Error: {str(e)}",
            "books": []
        }
