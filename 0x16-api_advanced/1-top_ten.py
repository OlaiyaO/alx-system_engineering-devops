#!/usr/bin/python3
"""Function to display the top 10 hot posts of a specific Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Display the titles of the 10 hottest posts from a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    data = response.json().get("data")
    [print(post.get("data").get("title")) for post in data.get("children")]
