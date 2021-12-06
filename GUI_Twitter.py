# -*- coding: utf-8 -*-
"""
Created on Mon 12/6/2021

@author: Rida Tariq

"""

from tkinter import *
from twitter_api import search_tweets
from reddit_api import get_data

class Coin():
    def __init__(self):
        window = Tk()
        window.title('Dashboard')
        window.geometry('1200x195')
        # text = Text (window)
        # text.tag_configure("tag_name", justify='center')
        window.configure(background='#FFFFFF')
        blue_color = '#DFF3F8'
        start = Label(window, text='Enter the number of posts you want to pull and hit, Click Me button :', background='#FFFFFF')
        start.grid(column=1, row=0)
        gap = Label(window, text='', background='#FFFFFF').grid(column=0, row=1)
        gap = Label(window, text='', background='#FFFFFF').grid(column=1, row=1)
        gap = Label(window, text='', background='#FFFFFF').grid(column=3, row=1)
        gap = Label(window, text='', background='#FFFFFF').grid(column=1, row=3)


        pennies = Label(window, text='No. of Tweets (10-100): ', background=blue_color).grid(column=0, row=2)
        # nickels = Label(window, text='Nickels: ', background='#FFFFCB').grid(column=0, row=9)
        # dollar = Label(window, text='Dollar coins: ', background='#FFFFCB').grid(column=0, row=6)
        
        tweets1 = Entry(window, width=12, background=blue_color)
        tweets1.grid(column=1, row=2)       
        
        # nickels1 = Entry(window, width=12, background='#FFFFCB')
        # nickels1.grid(column=1, row=9)
                
        # dollar1 = Entry(window, width=12, background='#FFFFCB')
        # dollar1.grid(column=1, row=6)
        
        pennies = Label(window, text='Twitter Data status: ', background=blue_color).grid(column=2, row=2)
        # nickels = Label(window, text='Nickel value: ', background='#FFFFCB').grid(column=2, row=2)
        # dollar = Label(window, text='Dollar coin value: ', background='#FFFFCB').grid(column=2, row=6)
        # total = Label(window, text='Total Change value: ', background='#FFFFCB').grid(column=2, row=7)
        
        pennies2 = Label(window, text='', background=blue_color)
        pennies2.grid(column=3, row=2)
        
        # nickels2 = Label(window, text='$0.00', background='#FFFFCB')
        # nickels2.grid(column=3, row=2)

        # dollar2 = Label(window, text='$0.00', background='#FFFFCB')
        # dollar2.grid(column=3, row=6)
        
        # total = Label(window, text='$0.00', background='#FFFFCB')
        # total.grid(column=3, row=7)
        
        def compute():
            num_tweets = int(tweets1.get())
            if num_tweets >= 0:
                tweets_dataset = search_tweets("bitcoin ransomware",num_tweets)
                tweets_dataset.to_csv("Twitter_dataset.csv", index = None)
                pennies2.config(text='%d tweets pulled & saved to Twitter CSV' %num_tweets)
                #reddit_dataset = get_data("bitcoin ransomware")
            else:
                error = Label(window, text='Invalid input for No. of Tweets.', background='#FFFFCB')
                error.grid(column=1, row=11)
                return
     
        
        button_twitter = Button(window, text='Twitter Pull', command=compute,
                                bg=blue_color, activebackground=blue_color,
                                height='1', width='15').grid(column=1, row=7)
        window.mainloop()

# Start of Code
if __name__ == "__main__":
    c1 = Coin()
    
    
