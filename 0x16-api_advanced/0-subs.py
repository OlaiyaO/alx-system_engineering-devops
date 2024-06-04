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

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    try:
        response = requests.get(url, headers=user_agent, allow_redirects=False)
        if response.status_code != 200:
            return 0

        results = response.json()
        return results.get('data', {}).get('subscribers', 0)

    except requests.RequestException:
        return 0
    except ValueError:  # JSON decoding failed
        return 0
