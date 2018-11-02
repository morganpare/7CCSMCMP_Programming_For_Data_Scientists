years_list=[1995,1996,1997,1998,1999]
third_birthday=years_list[3]
print third_birthday
oldest=years_list[-1]
print oldest

things=['mozzarella','cinderella','salmonella']
things[1]=things[1].title()
print things
things[0]=things[0].upper()
print things
things.remove('salmonella')
print things

suprise=['Groucho','Chico','Harpo']
suprise[2]=suprise[2].lower()[::-1].title()
print suprise

e2f={'dog':'chien','cat':'chat','walrus':'morse'}
print e2f.items()
f2e=dict((v,k) for k,v in e2f.items())
print f2e.items()
english=set(e2f.keys())
print english

cats=['Henri','Grumpy','Lucy']
animals={'cats':cats,'octopi':dict(),'emus':dict()}
print animals
life={'animals':animals,'plants':dict(),'other':dict}
print life

print life.keys()
print life['animals'].keys()
print life['animals']['cats']
