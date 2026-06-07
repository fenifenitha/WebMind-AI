import requests
from bs4 import BeautifulSoup


def scrape_website(url: str):

    try:

        response = requests.get(
            url,
            timeout=10,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        title = soup.title.string if soup.title else "No Title"

        paragraphs = []

        for paragraph in soup.find_all("p"):

            text = paragraph.get_text(strip=True)

            if text:
                paragraphs.append(text)

        content = " ".join(paragraphs)

        return {
            "success": True,
            "title": title,
            "content": content[:5000]
        }

    except Exception as error:

        return {
            "success": False,
            "message": str(error)
        }