#!/usr/bin/python3
"""
Queries the Reddit API recursively and returns a list containing the titles of all hot articles for a given subreddit.

Usage: recurse(subreddit, hot_list=[])
"""

import requests

def recurse(subreddit, hot_list=[]):
    """
    Queries the Reddit API recursively and returns a list containing the titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to store the titles of hot articles.

    Returns:
        list: A list containing the titles of all hot articles, or None if no results are found.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {'User-Agent': 'my-reddit-client/1.0'}  # Set a custom User-Agent

    params = {'limit': 100, 'after': None}
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()

        data = response.json()

        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
            for post in posts:
                hot_list.append(post['data']['title'])

            after = data['data']['after']
            
            if after:
                # Recursively call the function with the 'after' parameter
                return recurse(subreddit, hot_list, after=after)
            else:
                # Base case: No more pages, return the final hot_list
                return hot_list

        else:
            return None

    except requests.exceptions.HTTPError as http_err:
        if response.status_code // 100 == 4:
            return None
        else:
            print("HTTP error occurred: {}".format(http_err))
            return None

    except Exception as err:
        print("An error occurred: {}".format(err))
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

