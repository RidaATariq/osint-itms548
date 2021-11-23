import praw
import hconfig

reddit = praw.Reddit(
    client_id=hconfig.client_id,
    client_secret=hconfig.client_secret,
    user_agent=hconfig.user_agent,
    username=hconfig.username,
    password=hconfig.password,
)
reddit.validate_on_submit = True # needed to avoid error


# Output score for the first 256 items on the frontpage
for submission in reddit.front.hot(limit=20):
    print(submission)
