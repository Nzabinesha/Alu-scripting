
n that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries Reddit API and prints titles of first 10 hot posts
    Prints None if subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Custom"}
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            print("None")
            return

        data = response.json().get("data")
        if not data:
            print("None")
            return

        children = data.get("children")
        if not children:
            print("None")
            return

        for child in children:
            title = child.get("data", {}).get("title")
            if title:
                print(title)

    except Exception:
        print("None")
