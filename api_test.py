#%%
import praw
from praw.models.listing.mixins import subreddit
import hconfig

reddit = praw.Reddit(
    client_id=hconfig.c_id,
    client_secret=hconfig.secret,
    user_agent=hconfig.agent,
    username=hconfig.usr,
    password=hconfig.pwd,
)
reddit.validate_on_submit = True  # needed to avoid error


subreddit = reddit.subreddit('all')
posts = {"posts": []}
for submisson in subreddit.search("(cryptocurrency AND ransomware AND hack)",
                                  limit=10,
                                  time_filter="all"):
    posts["posts"].append({
        "subreddit": submisson.subreddit,
        "title": submisson.title,
        "num_comments": submisson.num_comments,
        "time_created": submisson.created_utc,
        "author": submisson.author,
        "post_id": submisson.id
    })

# print(posts)


# %%
