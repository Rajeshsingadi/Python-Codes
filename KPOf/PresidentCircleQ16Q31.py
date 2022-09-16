#Referring Josephs algorithm based 
#Method 1
#Time Complexity is O(n)

# def classPresident(num, k):
#     if num == 1:
#         return 1
#     else: 
#         return ( classPresident(num-1, k)+ k-1 ) % num+ 1
# arr= [1,2,3,4,5,6,7]
# k=5
# l = len(arr)

# IndexValue = classPresident(l, k)
# print(arr[IndexValue-1])


#Method 2
#Time complexity is O(N)
def classPresident(arr, k):
    k = k-1
    indx = k
    if indx > len(arr):
        indx = len(arr)- indx
    while len(arr) > 1:
        arr.pop(indx)
        indx = (indx + k) % len(arr)
    return arr[indx]


arr= [1,2,3,4]
k = 2
res = classPresident(arr, k)
print(res)

