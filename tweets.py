from utils import *
import requests
import pandas as pd


def get_tweet(search_query, fields, max_results, next, bearer_token=BEARER_TOKEN):
    headers = {"Authorization": f"Bearer {bearer_token}"}
    url = f"https://api.twitter.com/2/tweets/search/recent?" \
          f"query={search_query}&max_results={max_results}&tweet.fields={fields}"
    if next is not None:
        url += f"&next_token={next}"
    response = requests.request("GET", url, headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def fetch():
    data = []
    next = None
    count = 0
    while True:
        count += 1
        response = get_tweet(search_query, tweet_fields, tweets_per_query, next, bearer_token=BEARER_TOKEN)
        data.extend(response.get("data", []))
        next = response.get("meta").get("next_token", None)
        if (next is None) or (count >= total_queries):
            break
    df = pd.DataFrame(data)
    df.author_id = df.author_id.astype('str')
    df.id = df.id.astype('str')
    return df

