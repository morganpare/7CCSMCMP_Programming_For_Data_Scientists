print 'hello world'

myname = 'Elizabeth'
print 'Hello ' + myname

my_first_name = 'Morgan'
my_last_name = 'Pare'
print 'Hello ' + my_first_name + ' ' + my_last_name

yourname = raw_input ('What is your name?: ')
print 'Hello ' + yourname

your_first_name = raw_input ('What is your first name?: ')
your_surname = raw_input ('What is your surname?: ')
print 'Hello ' + your_first_name + ' ' + your_surname

n = raw_input('Enter a number: ')
print('You entered' + n)
n = float(n)
n3 = n * 3
print('Three times your number = ' + str(n3))

ten = int(10)
num = raw_input('Please enter an integer: ')
num = int(num)
print('You entered' + str(num))
print 'The mathematical operators applied to your number and 10 are:'
print(str(num) + ' + ' + str(ten) + ' = ' + str(ten+num))
print(str(num) + ' - ' + str(ten) + ' = ' + str(ten-num))
print(str(num) + ' * ' + str(ten) + ' = ' + str(ten*num))
print(str(num) + ' ^ ' + str(ten) + ' = ' + str(ten^num))
print(str(num) + ' / ' + str(ten) + ' = ' + str(ten/num))
print(str(num) + ' % ' + str(ten) + ' = ' + str(ten%num))

num1 = raw_input('Please enter an integer: ')
num1 = int(num1)
num2 = raw_input('Please enter another integer: ')
num2 = int(num2)
print('You entered' + str(num1) + str(num2))
print(str(num1) + ' == ' + str(num2) + ' : ' + str(num1==num2))
print(str(num1) + ' != ' + str(num2) + ' : ' + str(num1!=num2))
print(str(num1) + ' > ' + str(num2) + ' : ' + str(num1>num2))
print(str(num1) + ' >= ' + str(num2) + ' : ' + str(num1>=num2))
print(str(num1) + ' < ' + str(num2) + ' : ' + str(num1<num2))
print(str(num1) + ' <= ' + str(num2) + ' : ' + str(num1<=num2))

num1 = raw_input('Please enter a string: ')
num1 = str(num1)
num2 = raw_input('Please enter another string: ')
num2 = str(num2)
print('You entered' + str(num1) + str(num2))
print(str(num1) + ' == ' + str(num2) + ' : ' + str(num1==num2))
print(str(num1) + ' != ' + str(num2) + ' : ' + str(num1!=num2))
print(str(num1) + ' > ' + str(num2) + ' : ' + str(num1>num2))
print(str(num1) + ' >= ' + str(num2) + ' : ' + str(num1>=num2))
print(str(num1) + ' < ' + str(num2) + ' : ' + str(num1<num2))
print(str(num1) + ' <= ' + str(num2) + ' : ' + str(num1<=num2))

A = True
B = False
print('| A = ' + str(A) + ' | not A = ' + str(not A) + ' |')
print('| A and B = ' + str(A and B) + ' | A and A = ' + str(A and A) + ' | B and B = ' + str(B and B) + ' |')
print('| A or B = ' + str(A or B) + ' | A or A = ' + str(A or A) + ' | B or B = ' + str(B or B) + ' |')

import random
n = random.random()
print 'n = ' + str(n)
i = 0
while i < 10:
    n = random.random()
    print 'n = ' + str(n)
    i = i + 1

import random
i = 0
while i < 10:
    n = random.randint(2,12)
    print 'n = ' + str(n)
    i = i + 1

import random
i = 0
while i < 10:
    n = random.randint(0,51)
    print 'n = ' + str(n)
    i = i + 1

import random
i  = random.randint(1,10)
print 'i = ' + str(i)
if (i<5):
    print 'i is less than 5'
else:
    print 'i is not less than 5'

import random
i  = random.randint(1,10)
print 'i = ' + str(i)
if (i<3):
    print 'i is less than 3'
elif (i<7):
    print 'i is between 3 and 6'
else:
    print 'i is greater than 6'

import random
i  = random.randint(0,100)
print 'i = ' + str(i)
if (i==0):
    print 'i is zero'
elif ((i%2)==0):
    print 'i is even'
else:
    print 'i is odd'

myword = raw_input('Enter a word: ')
print('You entered: ' + myword)
i = myword.find('A')
if (i>-1):
    res=True
else:
    res=False
print('res = ' + str(res))

myword = raw_input('Enter a word: ')
print('You entered: ' + myword)
a = myword.find('A')
e = myword.find('E')
i = myword.find('I')
o = myword.find('O')
u = myword.find('U')
if (a>-1 or e>-1 or i>-1 or o>-1 or u>-1):
    res=True`
else:
    res=False
print('res = ' + str(res))

import random
i = random.randint(0,51)
print ('i is: ' + str(i))
# assign the suit
if (i<=12):
    suit='Diamonds'
elif (i<=25):
    suit='Clubs'
elif (i<=38):
    suit='Hearts'
elif(i<=51):
    suit='Spades'
else:
    suit='Error'
# assign the value
if ((i % 13)<=8):
    value=str(i+2)
elif ((i % 13)==9):
    value = 'Jack'
elif ((i % 13)==10):
    value = 'Queen'
elif ((i % 13)==11):
    value = 'King'
elif ((i % 13)==12):
    value = 'Ace'
else:
    suit = 'Error'
print(value + ' of ' + suit)

myword = raw_input('Enter a word: ')
print 'you entered' + myword
L= len(myword)
print ('Your word is ' + str(L) + ' letters long')
for i in range (0,L):
    print ('The ' + str(i) + 'th letter is ' + str(myword[i]))

myword = raw_input('Enter a word: ')
print 'you entered' + myword
c=0
L= len(myword)
vowels = {'a','e','i','o','u','A','E','I','O','U'}
print ('Your word is ' + str(L) + ' letters long')
for i in range (0,L):
    if myword[i] in vowels:
        c = c+1
print (myword + ' has ' + str(c) + ' vowels')

mynum = raw_input('Enter a number: ')
mynum = int(mynum)
while (mynum!=99):
    print(str(mynum))
    mynum = raw_input('Enter a number: ')
    mynum = int(mynum)
print('done')

mynum = raw_input('Enter a number: ')
l=[int(mynum)]
while (mynum!=str(99)):
    if (mynum=='quit'):
        break
    print(str(mynum))
    mynum = raw_input('Enter a number: ')
    l.append(int(mynum))
print('done')
print str(sum(l))

import random
c = 0
while c < 5:
    i = random.randint(0,51)
    # print ('i is: ' + str(i))
    # assign the suit
    if (i<=12):
        suit='Diamonds'
    elif (i<=25):
        suit='Clubs'
    elif (i<=38):
        suit='Hearts'
    elif(i<=51):
        suit='Spades'
    else:
        suit='Error'
    # assign the value
    if ((i % 13)<=8):
        value=str(i+2)
    elif ((i % 13)==9):
        value = 'Jack'
    elif ((i % 13)==10):
        value = 'Queen'
    elif ((i % 13)==11):
        value = 'King'
    elif ((i % 13)==12):
        value = 'Ace'
    else:
        suit = 'Error'
    print(value + ' of ' + suit)
    c += 1
