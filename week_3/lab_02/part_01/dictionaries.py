## Dictionaries
### Medal Table

country = 'Great Britain'
medals = {'country':'Great Britain', 'gold':64,'silver':39,'bronze':44}

print medals['gold']

for key in medals:
    print '%s won %s %s medals' % (country, medals[key], key)

total_medals = medals['gold'] + medals['silver'] + medals['bronze']

print '%s won %s total medals' % (country, total_medals)

medals_list = \
[{'country':'Great Britain', 'gold':64,'silver':39,'bronze':44}, \
{'country':'China', 'gold':107,'silver':81,'bronze':51}, \
{'country':'Ukraine', 'gold':41,'silver':37,'bronze':39}, \
{'country':'United States', 'gold':40,'silver':44,'bronze':31}, \
{'country':'Australia', 'gold':22,'silver':30,'bronze':29}]

for key in medals_list:
    total_medals = key['gold'] + key['silver'] + key['bronze']
    key['total_medals'] = total_medals

print medals_list

def medal_table():
    print ' The total number of medals:'
    for key in medals_list:
        country = key['country']
        total_medals = key['total_medals']
        print '%s = %s' % (country,total_medals)

medal_table()
