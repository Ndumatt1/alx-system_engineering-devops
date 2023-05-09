#!/usr/bin/python3
'''
This module queries the Reddit API and return the number of total subscriberss
'''
import requests


def number_of_subscribers(subreddit):
    ''' Returns number of total subscribers for a given subreddit '''
    if not subreddit:
        return 0
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    request = requests.get(url, headers={'User-Agent': 'folio'})
    if not request:
        return 0
    response = request.json()['data']['subscribers']
    return response
