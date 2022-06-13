# Method 1
def isPowerofTen(num):
    if num == 10:
        return True
    pow = 1
    while pow<num:
        pow = pow*10
        
    return pow==num

num = 100
print(isPowerofTen(num))


#Method 2
# import math
# def isPowerofTen(num):
#     p = math.log10(num)
#     if num == 10**math.floor(p):
#         return True
#     else:
#         return False

# num = 1000000
# print(isPowerofTen(num))