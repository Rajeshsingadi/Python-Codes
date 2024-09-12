l = ['a', 'b', 'c']

# method1
print(l[::-1])

#method2
print(list(reversed(l)))

#method3
s= ''
for i in l:
    s = i + s
print(s)
