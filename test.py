import json
import pandas as pd
import requests

server_ip = "13.213.46.166"
port = "30000"
api_key = "IJHXvVKglhWypDgq12mQWm2lp"
verbose = True


def get_all_tweets(fileName="tweets"):
    rsp = requests.get(url=f"http://{server_ip}:{port}/get_tweets",
                       headers={"apiKey": api_key})
    if rsp.status_code == 200:
        df = pd.DataFrame(json.loads(rsp.content))
        df.to_csv(f"{fileName}.csv", index=False)
        if verbose: print(f"Data fetched and stored in file named '{fileName}'")
    else:
        if verbose: print(f"Error in fetching data: status <{rsp.status_code}>")


def get_tweets_by_tag(tag, fileName="tag_search"):
    rsp = requests.get(url=f"http://{server_ip}:{port}/search_by",
                       headers={"apiKey": api_key},
                       params={"tag": tag})
    if rsp.status_code == 200:
        df = pd.DataFrame(json.loads(rsp.content))
        df.to_csv(f"{fileName}.csv", index=False)
        if verbose: print(f"Data fetched and stored in file named '{fileName}'")
    else:
        if verbose: print(f"Error in fetching data: status <{rsp.status_code}>")


if __name__ == '__main__':
    get_all_tweets(fileName="all_tweets")
    get_tweets_by_tag(tag= "bitcoin", fileName="bitcoin_tweets")

