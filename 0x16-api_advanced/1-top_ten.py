#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.

Usage: top_ten(subreddit)
"""

import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'my-reddit-client/1.0'}  # Set a custom User-Agent

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()

        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
            for post in posts:
                print(post['data']['title'])

        else:
            print(None)

    except requests.exceptions.HTTPError as http_err:
        if response.status_code // 100 == 4:
            print(None)
        else:
            print("HTTP error occurred: {}".format(http_err))

    except Exception as err:
        print("An error occurred: {}".format(err))

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit_name = sys.argv[1]
        top_ten(subreddit_name)
