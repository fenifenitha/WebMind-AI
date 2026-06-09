from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.services.crawler import WebsiteCrawler
from app.services.chunker import TextChunker

from app.services.scraper import scrape_website


app = FastAPI(
    title="WebMind AI"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class WebsiteRequest(BaseModel):
    url: str


@app.get("/")
def home():

    return {
        "message": "Backend Running"
    }


@app.post("/scrape")
def scrape(data: WebsiteRequest):

    return scrape_website(data.url)
@app.post("/crawl")
def crawl_website(data: dict):

    crawler = WebsiteCrawler()

    urls = crawler.crawl(
        data["url"]
    )

    return {
        "success": True,
        "total_pages": len(urls),
        "pages": urls
    }
@app.post("/chunk")
def chunk_text(data: dict):

    chunker = TextChunker()

    chunks = chunker.create_chunks(
        data["text"]
    )

    return {
        "success": True,
        "total_chunks": len(chunks),
        "chunks": chunks
    }