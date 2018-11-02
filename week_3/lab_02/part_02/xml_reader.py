import xml.etree.ElementTree as et

try:
    tree = et.ElementTree(file = "movies.xml")
    root = tree.getroot()
    for child in root:
        print("tag: '%s' attributes: %s text: '%s'" % (child.tag, child.attrib, child.text.strip()))
        for grchild in child:
            print("- tag: '%s' attributes: %s text: '%s'" % (grchild.tag, grchild.attrib,grchild.text.strip()))
except Exception as e:
    print ("error %s" % e)

try:
    tree = et.ElementTree(file = "movies.xml")
    root = tree.getroot()
    for child in root:
        # print("tag: '%s' attributes: %s text: '%s'" % (child.tag, child.attrib, child.text.strip()))
        for grchild in child:
            print("%s: '%s'" % (grchild.tag,grchild.text.strip()))
except Exception as e:
    print ("error %s" % e)

try:
    tree = et.ElementTree(file = "movies.xml")
    root = tree.getroot()
    movie_list = []
    for child in root:
        # print("tag: '%s' attributes: %s text: '%s'" % (child.tag, child.attrib, child.text.strip()))
        movie_dict = {}
        for grchild in child:
            if grchild.tag == 'Actors':
                actors = []
                for grgrchild in grchild:
                    actors.append(grgrchild.text.strip())
                movie_dict[grchild.tag] = ', '.join(actors)
            elif grchild.tag == 'Writers':
                writers = []
                for grgrchild in grchild:
                    writers.append(grgrchild.text.strip())
                movie_dict[grchild.tag] = ', '.join(writers)
            else:
                movie_dict[grchild.tag] = grchild.text.strip()
            # print("%s: '%s'" % (grchild.tag,grchild.text.strip()))
        movie_list.append(movie_dict)
except Exception as e:
    print ("error %s" % e)

print movie_list
