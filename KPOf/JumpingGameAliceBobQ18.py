 #Number of jumps made by alice is N
 #Number of jumps made by bob is M
 #GCD of M and N gives the 

def JumpGame(N,M):
    if N ==0:
        return M
    if M==0:
        return N
    if N>M:
        return JumpGame(N-M, M)
    else:
        return JumpGame(N, M-N)

N = 10
M = 35
print(JumpGame(N,M))


#----------------
#Method 2

# import math
# def JumpGame(N,M):
#     if N ==0:
#         return M
#     if M==0:
#         return N
#     if N>M:
#         return math.gcd(N-M, M)
#     else:
#         return math.gcd(N, M-N)

# N = 10
# M = 35
# print(JumpGame(N,M))