import praw
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

    return rv

def to_csv(data):
    pass