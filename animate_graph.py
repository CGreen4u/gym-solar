import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import os
import time
import pandas as pd
from pandas.io.common import EmptyDataError

os.chdir(r"C:\Users\cgree\Documents\Astra\Space_weather5_22\weakley_all")
style.use('fivethirtyeight')

fig, ax = plt.subplots()

##fig = plt.figure()
#ax = fig.add_subplot(1,1,1)

original_file = pd.read_csv('example.txt')
graph_data = pd.read_csv('example2.txt')
date = []
point = []
def animate(i):
    ax.set_xticklabels(date, rotation=45)
    for row1, index1 in graph_data.iterrows():
        print(index1[1])
        #time.sleep(10)
        date.append(index1[0])
        point.append(float(index1[1]))
        break
    if len(date) > 30:
        date.remove(date[0])
        point.remove(point[0])
    graph_data.drop(row1, inplace=True)
    ax.clear()
    ax.plot(date, point)


ani = animation.FuncAnimation(fig, animate,frames=10, interval=1000) #milliseconds every second it updates
plt.show()




##def __init__(self):
##    self.date = []
##    self.point = []
##    self.original_file = pd.read_csv('example.txt')
##    self.graph_data = pd.read_csv('example2.txt')
##    
##    os.chdir(r"C:\Users\cgree\Documents\Astra\Space_weather5_22\weakley_all")
##    style.use('fivethirtyeight')
##
##def animate(self):
##    fig, ax = plt.subplots()
##    self.ax.set_xticklabels(date, rotation=45)
##    for row1, index1 in self.graph_data.iterrows():
##        print(index1[1])
##        #time.sleep(10)
##        self.date.append(index1[0])
##        self.point.append(float(index1[1]))
##        break
##    if len(date) > 30:
##        self.date.remove(date[0])
##        self.point.remove(point[0])
##    self.graph_data.drop(row1, inplace=True)
##    self.ax.clear()
##    self.ax.plot(date, point)
##
##
##ani = animation.FuncAnimation(fig, animate,frames=10, interval=1000) #milliseconds every second it updates
##plt.show()
