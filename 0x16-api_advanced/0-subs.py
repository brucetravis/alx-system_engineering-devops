#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of
subscribers for a given subreddit.

Usage: number_of_subscribers(subreddit)
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of
subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'my-reddit-client/1.0'}  # Set a custom User-Agent

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers

    except requests.exceptions.HTTPError as http_err:
        if response.status_code // 100 == 4:
            return 0  # Return 0 for invalid subreddit
        else:
            print("HTTP error occurred: {}".format(http_err))
            return 0

    except Exception as err:
        print("An error occurred: {}".format(err))
        return 0


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit_name = sys.argv[1]
        subscribers_count = number_of_subscribers(subreddit_name)
        print(subscribers_count)
