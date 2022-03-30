import json
import pandas as pd
import requests


rsp = requests.get(url="http://127.0.0.1:30000/get_tweets",
                   headers={"apiKey": "IJHXvVKglhWypDgq12mQWm2lp"})
print("all", rsp.status_code)
if rsp.status_code == 200:
    df = pd.DataFrame(json.loads(rsp.content))
    df.to_csv("tweets.csv", index=False)


rsp = requests.get(url="http://127.0.0.1:30000/search_by",
                   headers={"apiKey": "IJHXvVKglhWypDgq12mQWm2lp"},
                   params={"tag": "bitcoin"})
print("search", rsp.status_code)
if rsp.status_code == 200:
    df = pd.DataFrame(json.loads(rsp.content))
    df.to_csv("tag_search.csv", index=False)
