#method 1
l=[1,2,3]
t=tuple(l)
print(t, type(t))

#method 2
st= ( *l,)

print(st, type(st))