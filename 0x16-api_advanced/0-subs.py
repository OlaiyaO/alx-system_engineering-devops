#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/JB)'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent, allow_redirects=False)
    
    if response.status_code != 200:
        return 0

    try:
        results = response.json()
        return results.get('data', {}).get('subscribers', 0)
    except ValueError:  # includes simplejson.decoder.JSONDecodeError
        return 0
