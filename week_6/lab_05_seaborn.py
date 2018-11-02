import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt
import seaborn as sns

sns.set_style("ticks")

""" load mpg to csv """
fuel = genfromtxt('fuel.csv', delimiter=',', dtype='float64')

# print (fuel[:5])

""" plot mpg """

mpg = fuel[:,0]
print(mpg)

sns.distplot(mpg,bins=20,kde=False,rug=True);
