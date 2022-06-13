s = "nirmal"

#Method 0
#Slicing
# print(s[::-1])

#Method 1
rs=''
for i in s:
    rs= i + rs
print(rs)

#Method 2
# rs=[]
# for i in range(len(s)-1,-1,-1):
#     rs.append(s[i])
# print(*rs, sep='')

#Method 3
# print(*reversed(s),sep='')

#Method 4(Words reverse)
# s="This is a string reverse program"
# l=[]
# for i in s:
#     l.insert(0,i)
# print(''.join(l))
