nuts = ['A', 'B', 'C', 'D']
bolts = ['D','C','A','B']
n=len(nuts)
hashkey = {}

for i in range(n):
    hashkey[nuts[i]] = i
# print(hashkey)
for i in range(n):
    if bolts[i] in hashkey:
        nuts[i] = bolts[i]
# print(nuts,bolts)
for i in range(n):
    print(nuts[i], end=' ')
print()
for j in range(n):
    print(bolts[j], end= ' ')