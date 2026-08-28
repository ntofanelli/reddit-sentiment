import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("SOCIALCRAWL_API_KEY")
URL = "https://socialcrawl.dev"
SUBREDDITS = ["wallstreetbets", "stocks", "StockMarket"]