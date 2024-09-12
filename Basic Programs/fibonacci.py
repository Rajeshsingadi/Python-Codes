def fib(num):
    n1,n2=0,1
    count=0
    if num<=0:
        print("Enter the input properly")
    elif num==1:
        print(n1)
    else:
        while(count<num):
            print(n1)
            nth=n1+n2
            n1=n2
            n2=nth
            count+=1

num= int(input("Enter no.of terms to print: "))

fib(num)

'''
#starting the number from 0
num=int(input("Enter a number to print fibonacci series till that number: "))
def fib(num):
    if num==0: return 0
    elif num==1: return 1
    else: return fib(num-1) + fib(num-2)

for i in range(num):
    print(fib(i), end=' ')                     
'''