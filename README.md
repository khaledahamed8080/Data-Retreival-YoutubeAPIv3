# Data-Retreival-YoutubeAPIv3

A Python-based backend service that retrieves YouTube video comments using the YouTube Data API, processes the response, stores the data locally as a CSV file, and exposes the results through a REST API.
This project demonstrates real-world backend and data handling patterns commonly used in **GenAI pipelines and MLOps systems**.

## Problem Statement

YouTube provides valuable user engagement data through comments, but extracting and persisting this data programmatically requires:
- Secure API integration
- Structured JSON processing
- Reliable data storage
- Clean API responses
This project focuses on building a **production-style API service** that handles these concerns end-to-end.

## Solution Overview

The application performs the following steps:
1. Calls the **YouTube Data API v3** to fetch top-level comments for a given video  
2. Extracts relevant comment text from the API response  
3. Stores the processed comments in a CSV file  
4. Returns the data as a structured JSON response via a Flask API  
This mirrors how real backend services ingest third-party data for analytics, ML pipelines, or downstream AI applications.

## Architecture / Flow

                                     Client Request
                                           ↓
                                       Flask API
                                           ↓
                                  YouTube Data API (v3)
                                           ↓
                                JSON Response Processing
                                           ↓
                          CSV File Storage + JSON HTTP Response


- Language: Python  
- Backend Framework: Flask  
- External API: YouTube Data API v3  
- Libraries: google-api-python-client, csv  
- Data Storage: CSV (local file system)

## Clone the repository
--bash
git clone https://github.com/your-username/youtube-comments-api.git
cd youtube-comments-api

## Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

## Install dependencies
pip install -r requirements.txt

##Configure YouTube API Key
Replace the API key in app.py:
DEVELOPER_KEY = "YOUR_YOUTUBE_API_KEY"

## Running the Application

# Start the Flask development server:
flask run

# The application will be available at:
http://127.0.0.1:5000/
