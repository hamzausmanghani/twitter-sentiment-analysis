import json
import pandas as pd
import requests

# utils
server_ip = "13.213.46.166"
# server_ip = "127.0.0.1"
port = "30000"
api_key = "IJHXvVKglhWypDgq12mQWm2lp"
verbose = True


def get_all_tweets(start, end):
    rsp = requests.get(url=f"http://{server_ip}:{port}/get_tweets",
                       headers={"apiKey": api_key},
                       params={"start": start, "end": end})
    if rsp.status_code == 200:
        df = pd.DataFrame(json.loads(rsp.content)['data'])
        file = f"tweets-{start}-{end}.csv"
        df.to_csv(file, index=False)
        if verbose: print(f"Data fetched and stored in file named '{file}'")
    else:
        if verbose: print(f"Error in fetching data: status <{rsp.status_code}>")


def get_tweets_by_tag(tag, start, end):
    rsp = requests.get(url=f"http://{server_ip}:{port}/search_by",
                       headers={"apiKey": api_key},
                       params={"tag": tag, "start": start, "end": end})
    if rsp.status_code == 200:
        df = pd.DataFrame(json.loads(rsp.content)['data'])
        file = f"{tag}-tweets-{start}-{end}.csv"
        df.to_csv(file, index=False)
        if verbose: print(f"Data fetched and stored in file named '{file}'")
    else:
        if verbose: print(f"Error in fetching data: status <{rsp.status_code}>")


if __name__ == '__main__':
    tag = "bitcoin"
    start = "2022-04-10"
    end = "2022-04-15"
    get_all_tweets(start, end)
    get_tweets_by_tag(tag, start, end)

