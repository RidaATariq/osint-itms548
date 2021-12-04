import matplotlib.pylab as plt
import csv

x = []
y = []
y_num = []
x_filtered = []

with open('reddit_dataset.csv','r') as reddit_csv:
	reddit_data = csv.reader(reddit_csv, delimiter = ',')
	next(reddit_csv)
	
	for row in reddit_data:
		x.append(row[1])
		y.append(row[4])
#print(y)
#print(y)

for i in y:
    j=int(i)
    y_num.append(j)

#y_num=[int(y) for i in y]
#print(y_num)

#y_num.sort()

myDict = {x[i]: y_num[i] for i in range(len(x))}
#print(myDict)
myList = myDict.items()
myList = sorted(myList)
x, y = zip(*myList)

##plt.bar(x, y_num, color = 'g', width = 0.72)
##plt.xlabel('Authors')
##plt.ylabel('Number of Comments')
##plt.title('Number of Comments per Author')
##plt.ylim([10, 100])
##plt.show()

plt.plot(x, y)
plt.show()
