#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles
of the first 10 hot posts for a given subreddit.

Usage: top_ten(subreddit)
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles
    of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'my-reddit-client/1.0'}  # Set a custom User-Agent

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()
        posts = data.get('data', {}).get('children', [])

        if not posts:
            print("No posts found.")
            return

        for post in posts[:10]:
            title = post['data']['title']
            print(title)

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print(f"Error: Subreddit '{subreddit}' not found.")
        else:
            print(f"HTTP error occurred: {http_err}")

    except Exception as err:
        print(f"An error occurred: {err}")


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit_name = sys.argv[1]
        top_ten(subreddit_name)
