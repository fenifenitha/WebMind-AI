from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

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