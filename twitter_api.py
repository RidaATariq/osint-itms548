import tweepy
import hconfig
import json
import pandas as pd


def twitter_client():
    client = tweepy.Client(bearer_token=hconfig.bearer_token,consumer_key=hconfig.consumer_key,consumer_secret=hconfig.consumer_secret,
                           access_token=hconfig.access_token, access_token_secret=hconfig.access_secret)
    return client

def search_tweets(keywords):
    client = twitter_client()
    tweets = client.search_recent_tweets(query=keywords, max_results=10, expansions='author_id',tweet_fields="entities")
    #tweets = client.search_recent_tweets(query=keywords, max_results=10, expansions='entities.hashtags.tag')
    #tweets = client.search_recent_tweets(query=keywords+" tweet.fields:entities", max_results=10)
    #tweets = client.search_recent_tweets(query=keywords, max_results=10, expansions='referenced_tweets.id')
    # print(tweets)


    data = tweets.data
    results = pd.DataFrame(columns = ['id','text'])

    if data:
        for tweet in data:
            obj = {}
            obj['id'] = tweet.id
            obj['text'] = tweet.text
            obj['author_id'] = tweet.author_id
            obj['entities'] = tweet.entities
            try:
                obj['username'] = tweet.entities['mentions'][0]['username']
            except Exception as e:
                obj['username'] = " "
            results = results.append(obj, ignore_index = True)

    else:
        return ''

    return results

tweets = search_tweets("bitcoin ransomware")
tweets.to_csv("Twitter_dataset.csv", index = None)
