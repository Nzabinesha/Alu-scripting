#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries Reddit API and prints titles of the first 10 hot posts
    If the subreddit is invalid, prints None
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "MyUserAgent"}
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return

        data = response.json().get("data", {}).get("children", [])
        for post in data:
            print(post["data"]["title"])
    except Exception:
        print(None)
