from fastapi import FastAPI

app = FastAPI(
    title="WebMind AI",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "status": "success",
        "message": "WebMind AI Backend Running"
    }