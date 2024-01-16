#!/usr/bin/python3
"""
Queries the Reddit API and returns the
number of subscribers for a given subreddit.

Usage: number_of_subscribers(subreddit)
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the
    number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'my-reddit-client/1.0'}  # Set a custom User-Agent

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print(f"Error: Subreddit '{subreddit}' not found.")
        else:
            print(f"HTTP error occurred: {http_err}")
        return 0

    except Exception as err:
        print(f"An error occurred: {err}")
        return 0


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit_name = sys.argv[1]
        subscribers_count = number_of_subscribers(subreddit_name)
        print(subscribers_count)
