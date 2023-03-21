import requests
import json


topic = 'ukraine'


URL = f'https://api.pushshift.io/reddit/comment/search/?q={topic}'

reddit_r = requests.get(URL)

comments_dict = {}


for i in range(10):
    print(reddit_r.json()['data'][i]['author'])
    print(reddit_r.json()['data'][i]['body'])
    print(reddit_r.json()['data'][i]['utc_datetime_str'])
    print('-' * 20, '\n')

for i in range(10):
    comments_dict[i] = {'author': reddit_r.json()['data'][i]['author']}
    comments_dict[i]['comment'] = reddit_r.json()['data'][i]['body']
    comments_dict[i]['utc'] = reddit_r.json()['data'][i]['utc_datetime_str']

for k, v in comments_dict.items():
    print(k, v)

with open('reddit_comments.json', 'w') as rj:
    json.dump(comments_dict, rj)
