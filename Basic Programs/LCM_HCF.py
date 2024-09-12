num1= int(input())
num2= int(input())

def HCF(num1,num2):
    if num2==0:
        return num1
    else:
        return HCF(num2,num1%num2)

def LCM(num1,num2):
    return num1*num2//(HCF(num1,num2))


lcm = LCM(num1,num2)
hcf=HCF(num1,num2)
print("LCM is: ", lcm)
print("HCF is: ", hcf)


"""
from math import gcd
print(gcd(24,15))
"""

