# main.py - Reddit Stock Sentiment Tracker



#Local project modules
from reddit_client import fetch_posts
from sentiment import analyze_sentiment
from database import init_db, save_post, avg_day_score



SUBREDDITS = ["wallstreetbets","stocks", "pennystocks"]
MIN_CHAR_LIMIT = 100

init_db()
print("Grabbing and analyzing posts from " + str(len(SUBREDDITS)) + " subreddit(s)... ")
posts = []
for sub in SUBREDDITS:

    post_sub = fetch_posts(sub, category="new", timeframe="day")

    for post in post_sub:
        if len(post) > MIN_CHAR_LIMIT:   # check str len
            score = analyze_sentiment(post)
            if score != -1:
                save_post(sub, score)



avg = avg_day_score()

if avg is None:
    print("No posts saved today.")
else:
    print("Today's average post score is " + str(avg))
    message = "Today's market sentiment is "
    # score 0 is neg 1 neutral 2 is positive
    if avg < 0.75:
        message += "bearish!"
    elif avg > 1.25:
        message += "bullish!"
    else: # neutral case
        message += "neutral!"
    print(message)
