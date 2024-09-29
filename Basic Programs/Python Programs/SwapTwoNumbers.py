#Python program to swap two number without using third variable

a = int(input("please give first number a: "))
b = int(input("please give second number b: "))
a=a-b
b=a+b
a=b-a
print("After swapping")
print("value of a is : ", a)
print("value of b is : ", b)


'''

Swapping of two numbers using third variable in Python language

a = int(input("please give first number a: "))
b = int(input("please give second number b: "))
tempvar=a
a=b
b=tempvar
print("After swapping")
print("value of a is : ", a);
print("value of b is : ", b); 
'''

'''
#Swaping

a = int(input("please give first number a: "))
b = int(input("please give second number b: "))
a, b = b, a
print("value of a is : ", a)
print("value of b is : ", b)

'''