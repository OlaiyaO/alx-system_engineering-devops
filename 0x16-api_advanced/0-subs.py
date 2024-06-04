#!/usr/bin/python3
"""Function for the number of subscribers for a specific Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Fetch and return the subscriber count of a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    data = response.json().get("data")
    return data.get("subscribers")