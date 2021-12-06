# -*- coding: utf-8 -*-
"""
Created on Mon 12/6/2021

@author: Rida Tariq

"""

from tkinter import *
from twitter_api import search_tweets
from reddit_api import get_data

class Dashboard():
    def __init__(self):
        
        def t_compute():
            num_tweets = int(tweets1.get())
            if num_tweets >= 0:
                tweets_dataset = search_tweets("bitcoin ransomware", num_tweets)
                tweets_dataset.to_csv("Twitter_dataset.csv", index = None)
                t_status.config(text='%d tweets pulled & saved to Twitter CSV' %num_tweets)
            else:
                error = Label(window, text='Invalid input for No. of Tweets.', background='#FFFFCB')
                error.grid(column=1, row=11)
                return
        
        def r_compute():
            num_posts = int(reddits1.get())
            if num_posts >= 0:
                reddit_dataset = get_data("bitcoin ransomware", num_posts)
                r_status.config(text='%d posts pulled & saved to Reddit CSV' %num_posts)

            else:
                error = Label(window, text='Invalid input for No. of Posts.', background='#FFFFCB')
                error.grid(column=1, row=11)
                return
        
        window = Tk()
        window.title('Dashboard')
        window.geometry('1200x195')

        window.configure(background='#FFFFFF')
        start = Label(window, text='Enter the number of tweets/posts to pull and hit, Click button:', background='#FFFFFF', font='Helvetica 15 bold')
        start.grid(column=1, row=0)
        gap = Label(window, text='', background='#FFFFFF').grid(column=0, row=1)
        gap = Label(window, text='', background='#FFFFFF').grid(column=1, row=1)
        gap = Label(window, text='', background='#FFFFFF').grid(column=3, row=1)
        gap = Label(window, text='', background='#FFFFFF').grid(column=1, row=3)
        gap = Label(window, text='', background='#FFFFFF').grid(column=0, row=5)
        gap = Label(window, text='', background='#FFFFFF').grid(column=1, row=5)
        gap = Label(window, text='', background='#FFFFFF').grid(column=2, row=5)
        gap = Label(window, text='', background='#FFFFFF').grid(column=3, row=5)
        gap = Label(window, text='', background='#FFFFFF').grid(column=1, row=7)
        
        # =============================================================================
        # Twitter IO
        # =============================================================================
        blue_color = '#DFF3F8'
        reddit_color = '#FFF3F8'


        tweet_label = Label(window, text='  No. of Tweets (10-100): ', background=blue_color).grid(column=0, row=2)

        tweets1 = Entry(window, width=12, background=blue_color)
        tweets1.grid(column=1, row=2)       
        
        t_label = Label(window, text='Twitter Data status: ', background=blue_color).grid(column=2, row=2)
        
        t_status = Label(window, text='', background=blue_color)
        t_status.grid(column=3, row=2)
        
        button_twitter = Button(window, text='Twitter Pull', command=t_compute,
                                bg=blue_color, activebackground=reddit_color,
                                height='1', width='15').grid(column=1, row=4)
        
        # =============================================================================
        # Reddit IO
        # =============================================================================

        reddit_label = Label(window, text='  No. of Posts (1-100): ', background=reddit_color).grid(column=0, row=6)

        reddits1 = Entry(window, width=12, background=reddit_color)
        reddits1.grid(column=1, row=6)       
        
        r_label = Label(window, text='Reddit Data status: ', background=reddit_color).grid(column=2, row=6)
        
        r_status = Label(window, text='', background=reddit_color)
        r_status.grid(column=3, row=6)

        button_reddit = Button(window, text='Reddit Pull', command=r_compute,
                                bg=reddit_color, activebackground=blue_color,
                                height='1', width='15').grid(column=1, row=8)
        
        
        
        window.mainloop()

# Start of Code
if __name__ == "__main__":
    d1 = Dashboard()
    
    
