import time

import requests
import json
import concurrent.futures
from timer_func import timer


topics = ['ukraine',
          'ai',
          'computer science',
          'space', 'universe',
          'internet',
          'pycharm']

comments_dict = {}


def get_comments(topic):

    """This function returns the most recent comments for the given topic"""

    URL = f'https://api.pushshift.io/reddit/comment/search/?q={topic}'
    reddit_r = requests.get(URL)

    topic_dict = {}

    for num in range(10):
        topic_dict[reddit_r.json()['data'][num]['author']] = {
            'comment': reddit_r.json()['data'][num]['body'],
            'time': reddit_r.json()['data'][num]['utc_datetime_str']}

    comments_dict[f'{topic}'] = topic_dict
    time.sleep(0.5)


@timer
def thread_func():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(get_comments, topics)

    with open('reddit_hw34.json', 'w') as rj:
        json.dump(comments_dict, rj)


if __name__ == "__main__":

    thread_func()
