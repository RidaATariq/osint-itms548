# -*- coding: utf-8 -*-
"""
@authors: Hareem Akram & Rida Tariq

"""

#!/usr/bin/python

import matplotlib.pylab as plt
import csv
from datetime import datetime, timezone
import pandas as pd
import seaborn as sns

def reddit_plot():
    reddit_x = []
    reddit_y = []
    reddit_y_num = []
    reddit_x_filtered = []
    dateList = []
    testList = []
    
    # open csv file generated using
    with open('reddit_dataset.csv','r') as reddit_csv:
    	reddit_data = csv.reader(reddit_csv, delimiter = ',')
    	next(reddit_csv)
    
    	for row in reddit_data:
    		reddit_x.append(row[1])
    		reddit_y.append(row[6])
    
    # convert all values in list y from str to int
    for i in reddit_y:
        j=int(float(i))
        reddit_y_num.append(j)
    
    for i in reddit_y_num:
            date_time_raw = datetime.fromtimestamp(i)
            post_date = datetime.date(date_time_raw)
            dateList.append(post_date)
    
    for i in range(len(dateList)):
            testList.append(i)
    
    plt.title("Reddit posts versus date/time")
    plt.ylabel('posts')
    plt.xlabel('date')
    plt.plot(dateList,testList)
    plt.show()

# Twitter plot
def twitter_plot():
    Tweet_data = pd.read_csv("Twitter_dataset.csv")
    Tweet_data['date_time'] = pd.to_datetime(Tweet_data['date_time'])
    print(Tweet_data.head())
    print(Tweet_data.columns)
    plt.figure()
    sns.scatterplot(x=Tweet_data['date_time'] ,y=Tweet_data.index)
    plt.ylabel('Tweets')
    plt.title("Tweets versus date/time")
    plt.xlabel("date/time")
    plt.show()
