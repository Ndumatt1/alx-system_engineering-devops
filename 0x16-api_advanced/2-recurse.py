#!/usr/bin/python3
''' This module queries the Reddit API '''
import requests


def recurse(subreddit, hot_list=[], after=None):
    ''' Returns a list containing the titles of all hot articles '''
    if not subreddit:
        return None
    if len(hot_list) >= 1000:
        return hot_list
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'folio'}
    params = {'limit': 100, 'after': after}
    request = requests.get(url, headers=headers, params=params)
    if not request:
        return None
    response = request.json()['data']
    after = response['after']
    titles = response['children']
    for title in titles:
        hot_list.append(title['data']['title'])
    if after is not None:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
    return None
