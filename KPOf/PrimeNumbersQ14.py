#Method 1
# print("Please enter a integer to get the list of list of primes til that entered num: ")
# num = int(input())
# def primeNumbers(num):
#     if num<=1:
#         return 0
#     else:
#         prime = [2]
#         counter = 3
#         while counter<=num:
#             for i in range(3, counter, 2):
#                 if counter % i == 0:
#                     counter  += 2
#                     break
#             else:
#                 prime.append(counter)
#                 counter  += 2
#         return prime

# p=primeNumbers(num)
# print(p)


#Check whether it is a prime number or not True or False.
#Time complexity is O(sqrt(N))
#Iterative approach
def is_prime(n):
    """
    Assumes that n is a positive natural number
    """
    # We know 1 is not a prime number
    if n <= 1:
        return False

    i = 2
    # This will loop from 2 to int(sqrt(x))
    while i*i <= n:
        # Check if i divides x without leaving a remainder
        if n % i == 0:
            # This means that n has a factor in between 2 and sqrt(n)
            # So it is not a prime number
            return False
        i += 1
    # If we did not find any factor in the above loop,
    # then n is a prime number
    return True
n=2
res=is_prime(n)
print(res)

#Method 2
# num = 10

# def primeNumbers(num):
#     prime=[]
#     if num<=1:
#         return 0
#     elif num == 2:
#         return 2
#     else:
#         for i in range(2, num):
#             for j in range(2,i):
#                 if i%j == 0:
#                     break
#             else:
#                 prime.append(i)

#         return prime
# p=primeNumbers(num)
# print(p)

#Method 3(Recursive)
#Method using recursion
num = 11
def primeNumbers(num, i=2):
    if num<=2:
        if num == 2:
            return True
        else:
            return False
    if num%i==0:
        return False
    if i*i >num:
        return True
    return primeNumbers(num, i+1)
        
        
p=primeNumbers(num)
if p:
    print("Prime Number")
else:
    print("Not a Prime Number")


# import math

# num = int(input())

# while num%2==0:
#     print(2)
#     num = num/2

# for i in range(3, int(math.sqrt(num))+1,2):
#     while num%i == 0:
#         print(i)
#         num = num/i

# if num>2:
#     print(num)
