num=list(map(int,input().split()))
n=num[0]
dif=num[1]
st=list(map(int,input().split()))
count=0
j=len(st)-1
for i in range(len(st)):
    if(st[i]!=st[j]):
        a=abs(st[i]-st[i+1])     
        if(a==dif):
            count+=1
print(count)


