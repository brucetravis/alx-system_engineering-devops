#!/usr/bin/python3
"""
Queries the Reddit API recursively, parses the title of all hot articles,
and prints a sorted count of given keywords.

Usage: count_words(subreddit, word_list)
"""

import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Recursively queries the Reddit API,
    parses the title of all hot articles,
    and prints a sorted count of given keywords.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of keywords to count.
        after (str): The Reddit API parameter for pagination.
        word_count (dict): A dictionary to store the count of each keyword.

    Returns:
        None
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
            print_results(word_count)
            return

        for post in children:
            title = post['data']['title']
            update_word_count(title.lower(), word_list, word_count)

        after = data['data'].get('after')
        count_words(subreddit, word_list, after, word_count)

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print(f"Error: Subreddit '{subreddit}' not found.")
        else:
            print(f"HTTP error occurred: {http_err}")

    except Exception as err:
        print(f"An error occurred: {err}")


def update_word_count(title, word_list, word_count):
    """
    Updates the word count dictionary based on
    the given title and word list.

    Args:
        title (str): The title of the Reddit post.
        word_list (list): A list of keywords to count.
        word_count (dict): A dictionary to store the count of each keyword.

    Returns:
        None
    """
    for word in word_list:
        word_lower = word.lower()
        if word_lower in title:
            word_count[word_lower] = word_count.get(word_lower, 0) + 1


def print_results(word_count):
    """
    Prints the sorted count of keywords.

    Args:
        word_count (dict): A dictionary containing the count of each keyword.

    Returns:
        None
    """
    sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_words:
        print(f"{word}: {count}")


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming'python java javascript'".format(sys.argv[0]))
    else:
        subreddit_name = sys.argv[1]
        word_list = sys.argv[2].split()
        count_words(subreddit_name, word_list)
