num=int(input())
for i in range(0,num):
    for j in range(1,num-i):
        print(" ",end="")
    for k in range(0,2*i+1):
        print("*",end="")
    print("")



