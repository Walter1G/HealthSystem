import axios from "axios";

const API = axios.create({
  baseURL: import.meta.env.VITE_API_URL,  // base url in .env
});

// Add token if available
API.interceptors.request.use((config) => {
  const token = localStorage.getItem("authToken");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default API;
