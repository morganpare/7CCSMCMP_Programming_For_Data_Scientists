import random

f = open('mydata.txt', 'w')
num = random.randint(44,126)
asc_num = chr(num)
f.write(asc_num)
f.close

f = open('mydata.txt','r')
mystring = f.read()
print (len(mystring))
f.close()
