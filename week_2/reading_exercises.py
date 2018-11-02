evens = [number for number in range(0,11,2)]
print evens

squares = {number:number**2 for number in range(11)}
print squares

odds = {number for number in range(10) if number % 2 == 1}
print odds

def good() :
    return ['Harry', 'Ron', 'Hermione']
print good()

n = ('roast beef', 'ham', 'head', 'clam')

poem = 'My kitty cat likes %s \n\
My kitty cat likes %s \n\
My kitty cat fell on his %s \n\
And now he thinks he\'s a %s' % n

print poem


test1 = 'This is a test of the emergency system'

fout = open('test1.txt','wt')
fout.write(test1)
fout.close

fin = open('test1.txt','rt')
test2 = fin.read()
fin.close()
print test2
print (test1 == test2)

text = 'author,book\n\
J R R Tolkien,The Hobbit\n\
Lynne Truss,"Eats, Shoots & Leaves"'

fout = open('books.csv','wt')
fout.write(test1)
fout.close
