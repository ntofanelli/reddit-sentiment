import os
from xml.etree.ElementTree import tostring

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("SOCIALCRAWL_API_KEY")
URL = "https://socialcrawl.dev/v1/reddit/"



def fetch_posts(subreddit, category="new", timeframe="day"):

        if not API_KEY:
            print("Error: SOCIALCRAWL_API_KEY is not sent.")
            return []

        #Auth Header
        headers = {
            'x-api-key': API_KEY
        }

        #Parameters required by SocialCrawl
        params = {
            "subreddit": subreddit,
            "category": category,
            "timeframe": timeframe
        }

        try:
            response = requests.get(URL + "subreddit", headers=headers, params=params,)

            response.raise_for_status()


            grabbed_urls = [item['post']['url'] for item in response.json()['data']['items']]


            textblocks = []
            for url in grabbed_urls:
                params = {
                    "url" : url
                }

                try:
                    response = requests.get(URL + "post", headers=headers, params=params)

                    response.raise_for_status()

                    text = response.json()['data']['post']['content']['text']
                    textblocks.append(text)

                except requests.exceptions.RequestException as e:
                    print(f"Failed to fetch r/{subreddit}: {e}")
                    return []
                if len(textblocks) > 5:
                    return textblocks
            return textblocks


        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch r/{subreddit}: {e}")
            return []
