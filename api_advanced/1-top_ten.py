#!/usr/bin/python3

import requests

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts of a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'SubredditTopTenViewer/1.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code != 200:
            print(None)
            return

        data = response.json()
        posts = data.get("data", {}).get("children", [])

        for post in posts:
            title = post.get("data", {}).get("title")
            print(title)

    except Exception:
        print(None)

