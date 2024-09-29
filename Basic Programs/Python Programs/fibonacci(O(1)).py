
import math
def fib(x):
    #we used formula for finding nth term of fibonacci series.
    # Formula Fn={[(√5+1)/2]∧n}/√5.
    #Above formula you wil get after solving Fn=Fn-1+Fn-2 on given initial condition F[0]=0,F[1]=1.
    n=(math.sqrt(5)+1)/2
    #round function used to round the value Ex:- round(3.2)=3 ,round(3.6)=4
    return round(math.pow(n,x)/math.sqrt(5))
n=int(input("enter the no of terms "))
for i in range(n):
    #end used for printing in single line
    print(fib(i),end=" ")


