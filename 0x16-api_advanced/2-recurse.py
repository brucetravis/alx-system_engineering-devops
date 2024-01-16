#!/usr/bin/python3
"""
Queries the Reddit API recursively and returns
a list of titles for all hot articles in a subreddit.

Usage: recurse(subreddit, hot_list=[])
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns
    a list of titles for all hot articles in a subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to store the titles of hot articles.
        after (str): The Reddit API parameter for pagination.

    Returns:
        list: A list containing the titles of all hot articles,
        or None if no results are found.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'my-reddit-client/1.0'}  # Set a custom User-Agent

    params = {'after': after} if after else {}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()

        data = response.json()
        children = data.get('data', {}).get('children', [])

        if not children:
            return hot_list if hot_list else None

        for post in children:
            title = post['data']['title']
            hot_list.append(title)

        after = data['data'].get('after')
        return recurse(subreddit, hot_list, after)

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print(f"Error: Subreddit '{subreddit}' not found.")
        else:
            print(f"HTTP error occurred: {http_err}")
        return None

    except Exception as err:
        print(f"An error occurred: {err}")
        return None


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit_name = sys.argv[1]
        result = recurse(subreddit_name)
        if result is not None:
            print(len(result))
        else:
            print("None")
