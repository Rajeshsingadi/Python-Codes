from itertools import permutations
string=input().split()
name=sorted(string[0])
num=int(string[1])
k= list(permutations(name,num))
for i in k:
    print(''.join(i))

