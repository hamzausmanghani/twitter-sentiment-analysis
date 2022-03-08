import json
import pandas as pd
from utils import *
import requests


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


search_query = "cryptocurrency"
tweet_fields = "text,author_id,created_at,lang"
data = []
next = None
count = 0

while(True):
    count += 1
    print(count)
    response = get_tweet(search_query, tweet_fields, 100, next, bearer_token=BEARER_TOKEN)
    data.extend(response.get("data", []))
    next = response.get("meta").get("next_token", None)
    if (next is None) or (count > 200):
        break

df = pd.DataFrame(data)
df.to_csv("samplev3.csv", index=False)



