#!/usr/bin/python3
''' This module queries the Reddit API'''
import requests


def top_ten(subreddit):
    ''' Prints the title of the first 10 hot posts for subreddit'''
    if not subreddit:
        print(None)
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    request = requests.get(url, headers={'User-Agent': 'folio'})
    if not request:
        print(None)
    else:
        response = request.json()['data']['children']
        for top_post in response:
            print(top_post['data']['title'])
