import multiprocessing
import time
import requests
import json
import concurrent.futures
import multiprocessing

topics = ['github',
          'planes',
          'rockets',
          'kyiv',
          'mooon',
          'chat gpt',
          'warp drive']


def timer_decorator(func):
    def wrapper():
        start = time.time()
        res = func()
        end = time.time()
        print(f"Execution time --> {round((end-start), 3)} seconds")
        return res
    return wrapper


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


@timer_decorator
def process_func():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(get_comments, topics)

    # with open('reddit.json', 'w') as rj:
    #     json.dump(dict_copy, rj)


if __name__ == "__main__":

    manager = multiprocessing.Manager()
    # Shared dict
    comments_dict = manager.dict()

    dict_copy = dict(comments_dict)

    process_func()

