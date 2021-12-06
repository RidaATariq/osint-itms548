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
        window = Tk()
        window.title('Dashboard')
        window.geometry('1200x195')

        window.configure(background='#FFFFFF')
        blue_color = '#DFF3F8'
        start = Label(window, text='Enter the number of posts you want to pull and hit, Click Me button :', background='#FFFFFF')
        start.grid(column=1, row=0)
        gap = Label(window, text='', background='#FFFFFF').grid(column=0, row=1)
        gap = Label(window, text='', background='#FFFFFF').grid(column=1, row=1)
        gap = Label(window, text='', background='#FFFFFF').grid(column=3, row=1)
        gap = Label(window, text='', background='#FFFFFF').grid(column=1, row=3)

        tweet_label = Label(window, text='No. of Tweets (10-100): ', background=blue_color).grid(column=0, row=2)

        tweets1 = Entry(window, width=12, background=blue_color)
        tweets1.grid(column=1, row=2)       
        
        t_label = Label(window, text='Twitter Data status: ', background=blue_color).grid(column=2, row=2)
        
        t_status = Label(window, text='', background=blue_color)
        t_status.grid(column=3, row=2)
        
        def compute():
            num_tweets = int(tweets1.get())
            if num_tweets >= 0:
                tweets_dataset = search_tweets("bitcoin ransomware",num_tweets)
                tweets_dataset.to_csv("Twitter_dataset.csv", index = None)
                t_status.config(text='%d tweets pulled & saved to Twitter CSV' %num_tweets)
                reddit_dataset = get_data("bitcoin ransomware")
            else:
                error = Label(window, text='Invalid input for No. of Tweets.', background='#FFFFCB')
                error.grid(column=1, row=11)
                return
     
        
        button_twitter = Button(window, text='Twitter Pull', command=compute,
                                bg=blue_color, activebackground=blue_color,
                                height='1', width='15').grid(column=1, row=4)
        window.mainloop()

# Start of Code
if __name__ == "__main__":
    d1 = Dashboard()
    
    
