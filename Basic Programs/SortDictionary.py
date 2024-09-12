dict = {}
dict['1'] = 'apple'
dict['3'] = 'orange'
dict['2'] = 'pango'

lst = dict.keys()

# Sorted by key
print("Sorted by key: ", sorted(lst))

dict = {}
dict['1'] = 'apple'
dict['3'] = 'orange'
dict['2'] = 'pango'

lst = dict.values()

#Sorted by value
print("Sorted by value: ", sorted(lst))


dict = {}
dict['1'] = 'apple'
dict['3'] = 'orange'
dict['2'] = 'strawberry'

lst = dict.items()

# Sorted by key
print("Sorted by key: ", sorted(lst, key = lambda x : x[0]))

#Sorted by value
print("Sorted by value: ", sorted(lst, key = lambda x : x[1]))