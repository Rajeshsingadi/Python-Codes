for i in range(int(input())):
    str=list(map(int,input().split()))
    num=str[1]
    lst=list(input().split())[0:str[0]]
    s=num%len(lst)
    p=len(lst)-s
    k=lst[p:]+lst[0:p]
    print(' '.join(k))