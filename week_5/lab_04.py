import numpy as np

data=np.random.randint(10,size=(6,8))

print(data)

print(data[3:,5:])

print(data[0:1])

print(data[:,1:3])

print(data[3:4,0:4])

print(np.mean(data, axis=0))

print(np.std(data, axis=0))

print(np.min(data, axis=0))

print(np.max(data, axis=0))

print(np.sort(data,axis=0))

data2=np.empty((15,4))
for i in range (15) :
    data2[i]=i

print(data2)

print(data2[[2,0,9,5],:])

data3=np.empty((1,4))
data3[0]=15

print(data3)

data4=np.empty((16,2))
for i in range(16):
    data4[i]=i

print(data4)

data5=np.concatenate((data2,data3),axis=0)

print(data5)

data6=np.concatenate((data5,data4),axis=1)

print(data6)

""" Titanic Data """

import csv as csv

try:
    with open('gender.csv','r') as fd:
        csv_handle=csv.reader(fd)
        csv_data=list(csv_handle)
except IOError as ioe:
    print ("IOError : " + str(ioe))

# print(csv_data)

gender = np.asarray(csv_data)

# print(gender)

try:
    with open('survived.csv','r') as fd:
        csv_handle=csv.reader(fd)
        csv_data=list(csv_handle)
except IOError as ioe:
    print ("IOError : " + str(ioe))

survived = np.asarray(csv_data)

# print(survived)


try:
    with open('titanicNumeric.csv','r') as fd:
        csv_handle=csv.reader(fd)
        csv_data=list(csv_handle)
except IOError as ioe:
    print ("IOError : " + str(ioe))

fares = [i[1] for i in csv_data]

print fares

fares=[i.strip() for i in fares]

print fares

fares_arr=np.asarray(fares,dtype=np.float64)

titanic_numeric = np.asarray(csv_data[1],dtype=np.float32)

print(titanic_numeric)

print(fares_arr.mean(axis=0))

num_male = (gender == 'male').sum()
num_female = (gender == 'female').sum()

print(num_male,num_female)

num_survived = (survived == '1').sum()
num_died = (survived == '0').sum()

print(num_survived,num_died)

female_survived = survived[gender == 'female']

print(female_survived)

num_female_survived = (female_survived == '1').sum()

print(num_female_survived)

import matplotlib.pyplot as plt

hist, bin_edges = np.histogram(fares, bins = range(5))

plt.bar(bin_edges[:-1], hist, width = 1)
plt.xlim(min(bin_edges), max(bin_edges))
plt.show()

try:
    with open('titanic.csv','r') as fd:
        csv_handle=csv.reader(fd)
        csv_data=list(csv_handle)
except IOError as ioe:
    print ("IOError : " + str(ioe))

titanic=np.asarray(csv_data)

print(titanic)

print(titanic.dtype)

print(titanic[0])

print(titanic[:,2])

print(np.unique(titanic[:,2]))

classes=titanic[:,2]

num_1 = (classes == '1').sum()
num_2 = (classes == '2').sum()
num_3 = (classes == '3').sum()
total = int(num_1) + int(num_2) + int(num_3)

print(num_1)
print(num_2)
print(num_3)

print(float(num_1)/float(total))
print(float(num_2)/float(total))
print(float(num_3)/float(total))

def mean_std(n):
    l =[]
    i = 0
    while i < n:
        l.append(np.random.normal())
        i+=1
    # print l
    l_arr=np.array(l)
    # print l_arr
    res_arr = np.array([np.mean(l_arr,axis=0),np.std(l_arr,axis=0)])
    return res_arr

print(mean_std(1000000))
