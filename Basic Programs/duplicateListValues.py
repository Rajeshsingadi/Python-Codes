l=[1,1,3,3,4,5,6,6,7,7,8,9]
nl=[]
for i in l:
    if l.count(i) >1:
        nl.append(i)

# duplicate values in the list
print(nl)

#refined the duplicate list
print(set(nl))
