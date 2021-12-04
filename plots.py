import matplotlib.pylab as plt
import csv
from datetime import datetime, timezone

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

# convert x and y lists to a dictionary
##redditDict = {reddit_x[i]: reddit_y_num[i] for i in range(len(reddit_x))}
##redditList = redditDict.items()
##redditList = sorted(redditList)
##x, y = zip(*redditList)

# creating line graph using dictionary
##plt.xlabel('Authors')
##plt.ylabel('Number of Comments')
##plt.plot(x, y)
##plt.show()

##for i in reddit_y:
##        datetime_obj = datetime.datetime.strptime(i, '%Y-%m-%d %H:%M:%S.%f')
##        reddit_y_num.append(datetime_obj)
##
##print(reddit_y_num)

for i in reddit_y_num:
        date_time_raw = datetime.fromtimestamp(i)
        post_date = datetime.date(date_time_raw)
        dateList.append(post_date)
##        print(post_date)
##        date_time_formatted = datetime(i).isoformat()
##        timestampList.append(date_time_formatted)

##print(dateList)

