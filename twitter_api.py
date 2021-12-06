import tweepy
import hconfig
import json
import pandas as pd

def twitter_client():
    client = tweepy.Client(bearer_token=hconfig.bearer_token,consumer_key=hconfig.consumer_key,consumer_secret=hconfig.consumer_secret,
                           access_token=hconfig.access_token, access_token_secret=hconfig.access_secret)
    return client

def search_tweets(keywords, maxresults=100):
    client = twitter_client()
    tweets = client.search_recent_tweets(query=keywords, max_results=maxresults, expansions='author_id',tweet_fields=["entities","created_at"])

    data = tweets.data
    results = pd.DataFrame(columns = ['id','text'])

    if data:
        for tweet in data:
            obj = {}
            obj['id'] = tweet.id
            obj['text'] = tweet.text
            obj['author_id'] = tweet.author_id
            #obj['entities'] = tweet.entities
            obj['date_time'] = tweet.created_at

            #This try except block tries to pull usernames
            try:
                obj['username'] = tweet.entities['mentions'][0]['username']
            except Exception as e:
                obj['username'] = " "

            #This try except block tries to pull all hashtags
            try:
                hashtags = []
                for hashtag_dict in tweet.entities['hashtags']:
                    hashtags.append(hashtag_dict['tag'])
                obj['hashtags'] = hashtags
            except Exception as e:
                obj['hashtags'] = " "

            results = results.append(obj, ignore_index = True)

    else:
        return ''

    return results

if __name__ == "__main__":
    tweets = search_tweets("bitcoin ransomware",50)
    tweets.to_csv("Twitter_dataset.csv", index = None)