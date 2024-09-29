num= int(input())
sum=0
for i in range(1, (num//2)+1):
    rem = num % i
    if rem==0:
        sum = sum + i
if sum == num:
    print("Perfect Number")
else:
    print("Not Perfect Number")



'''
Lets understand it with example

6 is a positive number and its divisor is 1,2,3 and 6 itself.

But we should not include 6 as by the definition of perfect number.

Lets add its divisor excluding itself

1+2+3 = 6 which is equal to number itself.

It means 6 is a Perfect Number.
'''