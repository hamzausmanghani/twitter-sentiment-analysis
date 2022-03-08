
import tweepy as tw


my_api_key = "IJHXvVKglhWypDgq12mQWm2lp"
my_api_secret = "bCbMpB0GNBvYHrUqUuowCW85yXLr9e9QFxPBRkOdVIEdbMFSIm"
# authenticate
auth = tw.OAuthHandler(my_api_key, my_api_secret)
api = tw.API(auth, wait_on_rate_limit=True)

print(api.search_tweets)

# search_query = "#covid19 -filter:retweets"
#
# tweets = tw.Cursor(api.search_tweets,
#               q=search_query,
#               lang="en",
#               since="2020-09-16").items(50)
# tweets_copy = []
# for tweet in tweets:
#     tweets_copy.append(tweet)


# print("Total Tweets fetched:", len(tweets_copy))

# the screen_name of the targeted user
screen_name = "geeksforgeeks"

# printing the latest 20 followers of the user
for follower in api.get_followers(screen_name):
    print(follower.screen_name)
