import requests
import json

TWITTER_URL = 'https://twitter.com/robots.txt'
WIKIPEDIA_URL = 'https://wikipedia.org/robots.txt'
GITHUB_URL = 'https://github.com/robots.txt'


# twitter robot.txt
treq = requests.get(TWITTER_URL)

# wikipedia robot.txt
wreq = requests.get(WIKIPEDIA_URL)

# github robot.txt
greq = requests.get(GITHUB_URL)


with open('twitter_robot.txt', 'w') as tf:
    tf.write(f"Here is data from {TWITTER_URL}: \n\n {treq.text}")

# with open('wikipedia_robot.txt', 'w') as wf:
#     wf.write(f"Here is data from {WIKIPEDIA_URL}: \n\n {wreq.text}")

with open('github_robot.txt', 'w') as gf:
    gf.write(f"Here is data from {GITHUB_URL}: \n\n {greq.text}")