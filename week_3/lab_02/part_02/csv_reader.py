import csv

try:
    with open("movies.csv","r") as movies_fd:
        csv_data = csv.reader(movies_fd)
        movies = list (csv_data)
except IOError as ioe:
    print ("IOError : " + str(ioe))

print movies

for i in movies:
    for j in range(len(movies[i])):
    if i == 0:
        pass
    else:
    if i[0] == 'Title':
        pass
    else:
        print 'Film Title: %s' % i[0]
        print 'Year: %s' % i[1]
        print 'Rated: %s' % i[2]
        print 'Released: %s' % i[3]
        print 'Runtime: %s' % i[4]
        print 'Genre: %s' % i[5]
        print 'Director: %s' % i[6]
        print 'Writers: %s' % i[7]
        print 'Actors: %s' % i[8]
        print 'Plot: %s' % i[9]

convert to a list of dictionaries
movies_dict = []

for i in movies:
    # for j in range(len(movies[i])):
    # if i == 0:
    #     pass
    # else:
    # if i[0] == 'Title':
    #     pass
    # else:
    movies_dict.append({\
    'Title':i[0],\
    'Year':i[1],\
    'Rated':i[2],\
    'Released':i[3],\
    'Runtime':i[4],\
    'Genre':i[5],\
    'Director':i[6],\
    'Writers':i[7],\
    'Actors':i[8],\
    'Plot':i[9],\
    'Language':i[10],\
    'Country':i[11],\
    'Awards':i[12],\
    'Poster':i[13],\
    'Metascore':i[14],\
    'imdbRating':i[15],\
    'imdbVotes':i[16],\
    'imdbID':i[17],\
    'Type':i[18],\
    'Response':i[19]\
    })

print movies_dict

'Title', 'Year', 'Rated', 'Released', 'Runtime', 'Genre', 'Director', 'Writers', 'Actors', 'Plot'

print str(len(movies) - 1)


try:
    with open("movies.csv","r") as movies_fd:
        csv_data = csv.DictReader(movies_fd,fieldnames = ['Title', 'Year', 'Rated', 'Released', 'Runtime', 'Genre', 'Director', 'Writers', 'Actors', 'Plot', 'Language', 'Country', 'Awards', 'Poster', 'Metascore', 'imdbRating', 'imdbVotes', 'imdbID', 'Type', 'Response'])
        next(csv_data)
        movies = list(csv_data)
except IOError as ioe:
    print ("IOError : " + str(ioe))

## Print key value pairs

for i in range(len(movies)):
    for key, value in movies[i].items():
        print '%s : %s' % (key, value)

def find_actor_movies(actor_name, movies_list = movies):
    print("Searching movies for actor: %s" % actor_name)
    movies_with_actor = []
    for i in movies:
        #create a set by splitting and stripping the actors field
        #if actor name in this set, add the title to a list
        if actor_name in set(x.strip() for x in i['Actors'].split(",")):
            # movies_with_actor.append(i['Title'])
            movies_with_actor.append(i)
    return movies_with_actor

movies_with_bogart = find_actor_movies("Humphrey Bogart")

with open("movies_with_actor.csv", "w") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = ['Title', 'Year', 'Rated', 'Released', 'Runtime', 'Genre', 'Director', 'Writers', 'Actors', 'Plot', 'Language', 'Country', 'Awards', 'Poster', 'Metascore', 'imdbRating', 'imdbVotes', 'imdbID', 'Type', 'Response'], extrasaction = 'ignore')
    writer.writeheader()
    writer.writerows(movies_with_bogart)

def find_actor_movies_partial(partial_actor_name, movies_list = movies):
    print("Searching movies for actor: %s" % partial_actor_name)
    movies_with_actor = []
    for i in movies:
        #create a set by splitting and stripping the actors field
        #if actor name in this set, add the title to a list
        actors = [x.strip() for x in i['Actors'].split(",")]
        actor_true = [s for s in actors if partial_actor_name in s]
        if not actor_true:
            pass
        else:
            # movies_with_actor.append(i['Title'])
            movies_with_actor.append(i)
        # matching = s for s in
    return movies_with_actor

print find_actor_movies_partial('umphrey')
print find_actor_movies_partial('Bergman')

def find_actor_movies_partial_upper(partial_actor_name, movies_list = movies):
    print("Searching movies for actor: %s" % partial_actor_name)
    movies_with_actor = []
    for i in movies:
        #create a set by splitting and stripping the actors field
        #if actor name in this set, add the title to a list
        actors = [x.strip().upper() for x in i['Actors'].split(",")]
        actor_true = [s for s in actors if partial_actor_name.upper() in s]
        if not actor_true:
            pass
        else:
            # movies_with_actor.append(i['Title'])
            movies_with_actor.append(i)
        # matching = s for s in
    return movies_with_actor

print find_actor_movies_partial_upper('uMphrey')
print find_actor_movies_partial_upper('BERGMAN')

def find_actor_movies(actor_name, movies_list = movies):
    print("Searching movies for actor: %s" % actor_name)
    movies_with_actor = []
    for i in movies:
        #create a set by splitting and stripping the actors field
        #if actor name in this set, add the title to a list
        if actor_name in set(x.strip() for x in i['Actors'].split(",")):
            # movies_with_actor.append(i['Title'])
            movies_with_actor.append(i)
    return movies_with_actor

def write_to_csv():
    try:
        with open("queries.csv","r") as queries_fd:
            csv_data = csv.DictReader(queries_fd,fieldnames = ['actor_name'])
            next(csv_data)
            queries = list(csv_data)
            print queries
            for i in queries:
                movies_with_query = find_actor_movies(i['actor_name'])
                with open("movies_with_%s.csv" % i['actor_name'].strip().replace(" ", "_").lower(), "w") as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames = ['Title', 'Year', 'Rated', 'Released', 'Runtime', 'Genre', 'Director', 'Writers', 'Actors', 'Plot', 'Language', 'Country', 'Awards', 'Poster', 'Metascore', 'imdbRating', 'imdbVotes', 'imdbID', 'Type', 'Response'], extrasaction = 'ignore')
                    writer.writeheader()
                    writer.writerows(movies_with_query)
    except IOError as ioe:
        print ("IOError : " + str(ioe))

write_to_csv()
