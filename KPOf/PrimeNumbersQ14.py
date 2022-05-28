#Method 1
print("Please enter a integer to get the list of list of primes til that entered num: ")
num = int(input())
def primeNumbers(num):
    if num<=1:
        return 0
    else:
        prime = [2]
        counter = 3
        while counter<=num:
            for i in range(3, counter, 2):
                if counter % i == 0:
                    counter  += 2
                    break
            else:
                prime.append(counter)
                counter  += 2
        return prime

p=primeNumbers(num)
print(p)



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
# num = 11

# def primeNumbers(num, i=2):
#     if num<=2:
#         if num == 2:
#             return True
#         else:
#             return False
#     if num%i==0:
#         return False
#     if i*i >num:
#         return True
#     return primeNumbers(num, i+1)
        
        
# p=primeNumbers(num)
# if p:
#     print("Prime Number")
# else:
#     print("Not a Prime Number")


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
