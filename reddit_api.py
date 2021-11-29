import praw
import csv
from hconfig import c_id, secret, usr, pwd, agent


# Reddit Functions
def credentials():
    reddit = praw.Reddit(
        username=usr,
        password=pwd,
        client_id=c_id,
        client_secret=secret,
        user_agent=agent,
    )
    return reddit


# function to pull data
def get_data(keywords):
    reddit = credentials()
    subreddit = reddit.subreddit("all")
    data_pool = subreddit.search(keywords, limit=None, time_filter="year")

    rv = {}
    for keywords in data_pool:
        # add the posts to our dict as they are being called
        rv[keywords.title] = {
            "post_id": keywords.id,
            "subreddit": keywords.subreddit,
            "title": keywords.title,
            "num_comments": keywords.num_comments,
            "author": keywords.author,
        }
        
    with open('testRedditFetch.csv', 'a') as f:
        headers = ['ID', 'Subreddit', 'Title', 'Number of Comments', 'Author']
        writer = csv.DictWriter(f, fieldnames=headers,
                                extrasaction='ignore', dialect='excel')
        writer.writeheader()
        for post in data_pool:
            data = {'ID: {}, Subreddit: {}, Title: {}, Number of comments: {}, Author: {}'.format(post,
                                                                                                  post.subreddit,
                                                                                                  post.title,
                                                                                                  post.num_comments,
                                                                                                  post.author)}
            print(writer.writerow(data))

    return rv


# def to_csv(data):
#     with open('testRedditFetch.csv', 'a') as f:
#         headers = ['ID', 'Subreddit', 'Title', 'Number of Comments', 'Author']
#         writer = csv.DictWriter(f, fieldnames=headers,
#                                 extrasaction='ignore', dialect='excel')
#         writer.writeheader()
#         for post in data:
#             data = {'ID: {}, Subreddit: {}, Title: {}, Number of comments: {}, Author: {}'.format(post,
#                                                                                                   post.subreddit,
#                                                                                                   post.title,
#                                                                                                   post.num_comments,
#                                                                                                   post.author)}
#             return writer.writerow(data)


# if __name__ == "__main__":
#     get_data(keywords="")
#     to_csv(get_data)
