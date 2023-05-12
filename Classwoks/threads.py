import requests
from requests.models import ReadTimeoutError
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from functools import wraps
from datetime import datetime
import threading

"""
task - compare execution time for running the check:
- no concurrency
- in 3 threads 
- in 10 threads
- in 5 processes"""


def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        all_time = end_time - start_time
        print(all_time)
        return result
    return wrapper


news_sites = [
    'https://www.nytimes.com/',
    'https://edition.cnn.com/',
    'https://www.bbc.co.uk/news',
    'https://www.huffingtonpost.com/',
    'https://abcnews.go.com/',
    'https://www.foxnews.com/',
    'https://www.nbcnews.com/',
    'https://time.com/',
    'https://www.FoxBusiness.com/',
    'https://theguardian.com',
    'https://www.cbsnews.com/',
    'https://USAToday.com',
    'https://Reuters.com/news ',
    'https://WSJ.com/']

def check_page_existence(page_url, timeout=2):
    try:
        response = requests.head(url=page_url, timeout=timeout)
        if response.status_code == 200:
            page_status = "exists"
        else:
            page_status = "does not exist"
    except ReadTimeoutError:
        page_status = "does not exist"

    return page_url + " - " + page_status

@decorator
def threadfunk(news_sites):
    with ThreadPoolExecutor(10) as executor:
        # execute tasks concurrently and process results in order
        executor.map(check_page_existence, news_sites)
            # report the result
            # print(result)
@decorator
def multifunc(news_sites):
    with ProcessPoolExecutor(5) as executor:
        # execute tasks concurrently and process results in order
        executor.map(check_page_existence, news_sites)

@decorator
def no_thread(news_sites):
    for i in news_sites:
        check_page_existence(i)

if __name__ == "__main__":
    print("No concurrency:")
    no_thread(news_sites)

    print("10 threads:")
    threadfunk(news_sites)

    print("5 processes:")
    multifunc(news_sites)

