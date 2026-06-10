# WebMind AI

## RAG Powered Website Chatbot

WebMind AI is a Retrieval-Augmented Generation (RAG) based chatbot that can understand website content and answer user questions using AI.

The system crawls websites, extracts content, chunks large documents, generates embeddings, stores data in a vector database, and provides intelligent responses using Gemini.



## Features

### Completed

* React Frontend Setup
* FastAPI Backend Setup
* Landing Page UI
* Website URL Processing
* Website Content Scraping
* Frontend and Backend Integration
* Recursive Website Crawling
* Internal Link Discovery
* Domain-Based URL Filtering
* Text Chunking Pipeline
* Recursive Character Text Splitting
* Gemini Embedding Generation
* Embedding API Endpoint
* Vector Preparation Pipeline

### Upcoming

* Qdrant Vector Database
* Semantic Search
* AI Chat Interface
* Source Citations
* PDF Knowledge Base Support



## Tech Stack

### Frontend

* React
* Vite

### Backend

* FastAPI
* Uvicorn

### Web Scraping

* Requests
* BeautifulSoup4

### Crawling

* Recursive Crawling
* Internal Link Discovery

### Chunking

* Recursive Character Text Splitter

### AI

* Gemini Embeddings
* Gemini LLM

### Vector Database

* Qdrant

### Similarity Search

* Cosine Similarity



## Project Architecture

React Frontend

↓

FastAPI Backend

↓

Crawler Service

↓

Website Scraper

↓

Chunking Service

↓

Embedding Service

↓

Qdrant Vector Database

↓

Retriever

↓

Gemini LLM

↓

Response Generator



## Project Structure

webmind-ai/

├── frontend/

│   ├── src/

│   │   ├── pages/

│   │   ├── services/

│   │   └── App.jsx

│

├── backend/

│   ├── app/

│   │   ├── services/

│   │   │   ├── scraper.py

│   │   │   ├── crawler.py

│   │   │   ├── chunker.py

│   │   │   └── embedder.py

│   │   └── main.py

│

└── README.md



## Current Workflow

User

↓

Enter Website URL

↓

React Frontend

↓

FastAPI Backend

↓

Crawler Service

↓

Discover Internal Links

↓

Website Scraper

↓

Extract Content

↓

Chunking Service

↓

Create Text Chunks

↓

Embedding Service

↓

Generate Gemini Embeddings

↓

Return Vector Data



## Development Progress

### Day 1

* Initialize Project Architecture
* React Setup
* FastAPI Setup
* Landing Page UI

### Day 2

* Website Scraping Module
* FastAPI API Integration
* Frontend Backend Connection
* Content Extraction using BeautifulSoup

### Day 3

* Recursive Website Crawler
* Internal Link Discovery
* Domain-Based URL Filtering
* URL Normalization
* Multi-Page Website Crawling
* Crawl API Endpoint

### Day 4

* Text Chunking Pipeline
* Recursive Character Text Splitter
* Chunk Processing Service
* Chunk API Endpoint
* Content Preparation for Embeddings

### Day 5

* Gemini Embedding Integration
* Google AI Studio API Setup
* Embedding Generation Service
* Embedding API Endpoint
* Vector Preparation Pipeline

### Next Step

* Qdrant Vector Database
* Vector Storage
* Semantic Retrieval
* Similarity Search



## Project Status

Current Phase: Embedding Generation Pipeline

### Completed

* Crawling
* Scraping
* Chunking
* Embedding Generation

### In Progress

* Qdrant Integration
* Semantic Retrieval



## Author

Fanitha TK

B.Tech Computer Science Engineering

Aspiring AI Engineer | Data Science Enthusiast


