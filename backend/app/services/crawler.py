from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup


class WebsiteCrawler:

    def __init__(self):
        self.visited_urls = set()

    def get_internal_links(self, url):

        links = []

        try:

            response = requests.get(
                url,
                timeout=10
            )

            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )

            base_domain = urlparse(url).netloc

            for tag in soup.find_all("a", href=True):

                href = tag["href"]

                full_url = urljoin(
                    url,
                    href
                )

                parsed_url = urlparse(
                    full_url
                )

                if parsed_url.netloc == base_domain:

                    if full_url not in links:

                        links.append(
                            full_url
                        )

        except Exception as error:

            print(
                f"Crawler Error: {error}"
            )

        return links

    def crawl(self, start_url, max_pages=10):

        pages = []

        urls_to_visit = [start_url]

        while urls_to_visit:

            current_url = urls_to_visit.pop(0)

            if current_url in self.visited_urls:
                continue

            self.visited_urls.add(
                current_url
            )

            pages.append(
                current_url
            )

            if len(pages) >= max_pages:
                break

            new_links = self.get_internal_links(
                current_url
            )

            for link in new_links:

                if link not in self.visited_urls:

                    urls_to_visit.append(
                        link
                    )

        return pages