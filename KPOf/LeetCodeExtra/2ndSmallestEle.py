# Q2. Find the second smallest element in an array. Important to take note of the word element
# For example, [4,8, 9, 2, 1, 1] should return 1, not 2. Also, if array.length is less than 2, just immediately return zero.

#Time Complexity is O(N)
def secondSmallest(l):
    l.sort()
    first = l[0]
    while first in l:
            l.remove(first)
    return l[0]
l=[4,8, 9, 2, 1, 2, 1, 1,9]

print(secondSmallest(l))

#Time Complexity is O(N)
# def secondSmallest(l):
#     first = 1e9
#     second = 1e9
#     for i in l:
#         if i<first:
#             second=first
#             first=i
#     for i in l:
#         if i<second and i!=first:
#             second=i
#     return second


# l=[4,8, 9, 2, 1, 2, 1, 1]
# l.sort()
# print(secondSmallest(l))