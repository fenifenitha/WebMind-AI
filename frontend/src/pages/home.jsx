import { useState } from "react";

function Home() {
  const [url, setUrl] = useState("");

  const handleProcess = () => {
    if (!url.trim()) {
      alert("Please enter a website URL");
      return;
    }

    console.log("Processing:", url);
  };

  return (
    <div className="container">
      <h1>WebMind AI</h1>

      <p className="subtitle">
        RAG Powered Website Chatbot
      </p>

      <div className="url-section">
        <input
          type="text"
          placeholder="Enter Website URL"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
        />

        <button onClick={handleProcess}>
          Process Website
        </button>
      </div>

      <div className="features">
        <div className="card">
          <h3>Website Crawling</h3>
          <p>Recursive Content Discovery</p>
        </div>

        <div className="card">
          <h3>Vector Search</h3>
          <p>Semantic Retrieval</p>
        </div>

        <div className="card">
          <h3>AI Chat</h3>
          <p>Gemini Powered Answers</p>
        </div>
      </div>
    </div>
  );
}

export default Home;