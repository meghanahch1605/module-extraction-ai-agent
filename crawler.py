import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def crawl_docs(base_url, max_pages=30):
    visited = set()
    pages = []

    def crawl(url):
        if url in visited or len(visited) >= max_pages:
            return
        visited.add(url)

        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.text, "lxml")
            pages.append((url, soup))

            for link in soup.find_all("a", href=True):
                href = link["href"]
                full_url = urljoin(base_url, href)

                if base_url in full_url:
                    crawl(full_url)

        except Exception as e:
            pass

    crawl(base_url)
    return pages
