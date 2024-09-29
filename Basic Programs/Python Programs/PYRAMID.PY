num=int(input())
for i in range(0,num):
    for j in range(num-i,1,-1):
        print(" ",end="")
    for k in range(0,i+1):
        print("* ",end="")
    '''
    for l in range(1,i):
        print("*",end="")'''
    print("")
for i in range(0,num):
    for m in range(0,i):
        print(" ",end="")
    for k in range(num-i,0,-1):
        print("* ",end="")
    '''
    for i in range(num-i-1,0,-1):
        print("*",end="")'''
    print("")
