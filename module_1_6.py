my_dict={'Anna':1999, 'Pit':1995, 'Kol':2000}
print(my_dict)
print(my_dict['Anna'])
print(my_dict.get('Jane', 'Такого ключа нет'))
my_dict.update({'Den':1994,'Kate':1996})
a=my_dict.pop('Den')
print(a)
print(my_dict)

my_set = {1,3,5,5,4,3,2,'стол', 'стул', 'стол'}
print(my_set)
my_set.add(9)
my_set.add(18)
my_set.discard(5)
print(my_set)

