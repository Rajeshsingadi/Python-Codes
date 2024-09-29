def fibbo(n):
    n1, n2 = 0, 1
    count = 0
    if n <= 0:
       print("Please enter a positive integer")
    elif n == 1:
       print(n2)
    else:
        while count < n:
           nth = n1 + n2
           n1 = n2
           n2 = nth
           count += 1
        print(n1)

def prime(n):
    count = 0
    for i in range(2, 99999):
        flag=0
        for j in range(2,i):
            if (i % j == 0):
                flag=1
                break
        if flag == 0:
            count+=1
            if count == n:
                print(i)
                break
 
# main
n = int(input())
if n%2 == 1:
    fibbo(n//2+1)
else:
    prime(n//2)