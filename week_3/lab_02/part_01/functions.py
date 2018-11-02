def check_input(num, min=0, max=10):
    if num < min or num > max:
        return False
    else:
        return True

# print check_input(1)
# print check_input(11)

def echo_input():
    num = ''
    while num != 'quit':
        num = raw_input ('Please enter a number: ')
        if check_input(int(num)):
            print str(num)
        else:
            print 'Please enter a number between 0 and 10'
    print 'Thanks for playing!'

echo_input()
