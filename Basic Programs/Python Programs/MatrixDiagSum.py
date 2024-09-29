n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().rstrip().split())))
print(arr)
dia1=[]
dia2=[]
for k in range(len(arr)):
   dia1.append(arr[k][k])
   dia2.append(arr[k][len(arr)-1-k])
print(sum(dia1+dia2))

