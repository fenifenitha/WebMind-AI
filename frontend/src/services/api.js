import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export const scrapeWebsite = async (url) => {

  const response = await axios.post(
    `${API_URL}/scrape`,
    {
      url: url,
    }
  );

  return response.data;
};