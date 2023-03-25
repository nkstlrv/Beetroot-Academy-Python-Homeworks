import asyncio
import aiohttp
import aiofiles
import json
import time

topics = ['asyncio',
          'coroutine',
          'global interpreter lock',
          'algorithms and data structures',
          'event loop',
          'json',
          'django']

result_dict = {}


async def get_comments(topic):
    url = f'https://api.pushshift.io/reddit/comment/search/?q={topic}'

    topic_dict = {}

    async with aiohttp.ClientSession() as session:
        reddit_resp = await session.get(url, ssl=False)
        data = await reddit_resp.json()

        for num in range(5):
            topic_dict[data['data'][num]['author']] = {
                'comment': data['data'][num]['body'],
                'time': data['data'][num]['utc_datetime_str']}

        result_dict[topic] = topic_dict


async def main():
    start = time.time()

    tasks = []

    for t in topics:
        task = asyncio.create_task(get_comments(t))
        tasks.append(task)

    await asyncio.gather(*tasks)

    end = time.time()

    async with aiofiles.open('async_reddit.json', 'w') as asj:
        await asj.write(json.dumps(result_dict))

    print(f'Execution time {round((end - start), 3)}')


if __name__ == "__main__":

    asyncio.run(main())
