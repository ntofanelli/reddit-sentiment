# main.py - Reddit Stock Sentiment Tracker


import os
from datetime import date
from collections import Counter

#Third Party
from dotenv import load_dotenv

#Local project modules
from reddit_client import fetch_posts
from sentiment import analyze_sentiment, score_to_label
from database import init_db, save_post, save_daily_summary