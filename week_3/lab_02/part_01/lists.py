## Lists
### Knitting exercise

import random

k = 'knit'
p = 'purl'

def knitting() :
    stitches = []
    for i in range(100):
        ran_num = random.randint(1,100)
        if ran_num % 2 == 0:
            stitches.append(k)
        else:
            stitches.append(p)
    return stitches

print knitting()

def knitting_while() :
    stitches = []
    i = 0
    while i <= 10:
        ran_num = random.randint(1,100)
        if ran_num % 2 == 0:
            stitches.append(k)
            i +=1
        else:
            stitches.append(p)
    return stitches

print knitting_while()

### Cards without replacement
#### Draw cardw without replacement
import random

def card_drawer_no_replacement(cards_to_draw = 10) :
    c = 0
    cards = []
    deck = [True] * 52
    # print deck
    while c < cards_to_draw:
        i = random.randint(0,51)
        # print ('i is: ' + str(i))
        # If exists in cards already then ignore
        if deck[i] == False:
            pass
        elif c > 51:
            break
        else:
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
                value=str((i%13)+2)
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
            # append to drawed cards list
            cards.append(value + ' of ' + suit)
            # Append to end of list
            c += 1
        deck[i] = False
    return (cards)

print card_drawer_no_replacement(52)
