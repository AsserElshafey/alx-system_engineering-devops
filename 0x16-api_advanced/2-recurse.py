#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    # Base case: invalid subreddit
    response = requests.get(f"https://www.reddit.com/r/{subreddit}/hot.json", headers={
                            "User-agent": "custom"}, params={"after": after})
    if response.status_code != 200:
        return None

    # Recursive case: valid subreddit
    data = response.json().get("data")
    children = data.get("children")
    after = data.get("after")
    for child in children:
        hot_list.append(child.get("data").get("title"))
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
