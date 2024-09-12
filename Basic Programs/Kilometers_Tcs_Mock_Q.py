count=1
l=[]
while count<99997779:
    k=input()
    if k=="q":
        break
    else:
        l.append(float(k))
        continue
    count+=1
sorted_List=[]
l.sort()
for i in l:
    if i<0:
        print("Invalid Input")
        exit()
    sorted_List.append(i)
print(sorted_List)
upd_List=[]
for i in sorted_List:
    if i!=42.195:
        upd_List.append(i)
print(upd_List[-3:][::-1])


'''

input:
42.195
42.195
42.195
33.25
40
41.2
38.9
37.5
q

output:
print last 3 highest except 42.195 highest distance
[41.2, 40.0, 38.9]

input:

33.33
42.9
39.56
-35.6
88.6
3.6
q

output: if the number is less than zero then print invalid input because 
 the kilometers should never be in negative

Invalid Input

'''