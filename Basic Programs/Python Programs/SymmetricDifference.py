# Enter your code here. Read input from STDIN. Print output to STDOUT
num1=int(input())
l1=set(map(int,input().split()))
num2=int(input())
l2=set(map(int,input().split()))
k=list(sorted(l1.symmetric_difference(l2)))
for i in range(len(k)):
    print(k[i])
print(*k,sep=" ")