import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt
# %matplotlib inline

""" load mpg to csv """
fuel = genfromtxt('fuel.csv', delimiter=',', dtype='float64')

print (fuel[:5])

""" plot mpg """

mpg = fuel[:,0].T

plt.plot(mpg)
plt.ylabel("mpg")
plt.xlabel("car_id")
plt.title("mpg of car models")
plt.axhline(y=25, color='r')
plt.show()

"""" plot mpg vs the gpm """

mpg = fuel[:,0].T
gpm = fuel[:,1].T

plt.scatter(mpg,gpm)
plt.xlabel("mpg")
plt.ylabel("gpm")
plt.title("plot of mpg vs. gpm")
plt.show()

""" plot histogram of WT """

print (fuel[:,2])

WT = np.unique(fuel[:,2]).T

plt.hist(WT,bins='auto')
plt.title("Histogram of the car weights")
plt.show()

""" plot box plot of mpg, gpm and wt """

all_data = fuel[:,0:3]

# rectangular box plot
bplot = plt.boxplot(all_data,
    vert=True, # vertical box aligmnent
    patch_artist=True) # fill with color
colors = ['pink', 'lightblue', 'lightgreen']
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)
print(bplot)
# adding horizontal grid lines
plt.grid(True)
# add labels
plt.xlabel('xlabel')
plt.ylabel('ylabel')
plt.show()

""" histogram of DIS based on ET """

et = fuel[:,7:]
dis = fuel[:,3:4]
# print (et)
dis_et_1 = dis[et==1]
dis_et_0 = dis[et==0]
# print (dis_et_1)
# print (dis_et_0)
plt.figure(1,figsize=(10,8))
plt.subplot(2,1,1)
plt.hist(dis_et_0,bins='auto')
plt.title("Histogram of the car DIS")
plt.subplot(2,1,2)
plt.hist(dis_et_1,bins='auto')
plt.show()

""" Number of cylinders histogram with label and annotation """

nc = fuel[:,4:5]
plt.hist(nc,bins='auto')
plt.title("Histogram of the Number of Cylinders")
plt.xlabel("Bin")
plt.ylabel("Frequency density")
plt.annotate('Largest bin', xy=(4.25,19), xytext=(6,20), arrowprops=dict(facecolor='black',shrink=0.05))
plt.ylim(0,24)
plt.show()

""" Scatter plot of mpg vs wt with colorbar of dis """

mpg = fuel[:,0].T
wt = fuel[:,2].T
dis = fuel[:,3].T

plt.scatter(mpg,wt,c=dis,s=100)
plt.xlabel("mpg")
plt.ylabel("wt")
plt.title("plot of mpg vs. wt with dis colobar")
plt.show()

""" line plots of mpg vs gpm and mpg vs log(gpm) """

mpg = fuel[:,0]
gpm = fuel[:,1]

plt.figure(1,figsize=(10,8))
plt.subplot(1,2,1)
plt.plot(mpg,gpm)
plt.xlabel("mpg")
plt.ylabel("gpm")
plt.title("mpg vs. gpm")
plt.grid(True)

plt.subplot(1,2,2)
plt.plot(mpg,gpm)
plt.yscale('log')
plt.xlabel("mpg")
plt.ylabel("log(gpm)")
plt.title("mpg vs. gpm")
plt.grid(True)

plt.show()
