import operator 
from functools import reduce
import numpy as np 

num=int(input("Enter any number:"))
def prime_numbers(num):
    prime=[]
    primes=[]
    n1,n2=0,1
    count=0
    counter=3
    if num<=0:
        print()
    elif num==1:
        primes.append(1)
    else:
        while(count<num):
            nth=n1+n2
            n1=n2
            n2=nth
            primes.append(n1)
            count+=1  

    while (counter<=num):
        for i in range(3,counter,2):
            if counter%i==0:
                counter=counter+2
                break
        else:
            prime.append(counter)
            counter=counter+2
    print(prime)
    print(primes)
    #print(reduce(operator.add, zip(primes,prime)))  
    print(np.array([[i, j] for i, j in zip(primes,prime)]).ravel())


prime_numbers(num)


