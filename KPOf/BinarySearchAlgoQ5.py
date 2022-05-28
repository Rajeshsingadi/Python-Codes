#without recursion Binary search time complexity is O(N)
def binarysearch(arr,key):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low<=high:
        mid = (low+high)//2
        if arr[mid]<key:
            low = mid+1
        elif arr[mid]>key:
            high = mid-1
        else:
            return mid
    return -1
arr = [5,7,9,13,32,33,42,54,56,88]
key =  33
res=binarysearch(arr,key)
if res!=-1:
    print("Element found at index: ",res)
else:
    print("Element not Found!")


# def binary_search(arr, start, end, key):
#     mid = (start + end)//2
#     if end>= start:
#         if arr[mid] == key:
#             return mid
#         elif arr[mid] > key:
#             return binary_search(arr, start, mid-1, key)
#         else:
#             return binary_search(arr, mid+1, end, key)
#     else:
#         return -1
    

# arr = [5,7,9,13,32,33,42,54,56,88]
# start = 0
# end = len(arr)-1
# key =  33

# index = binary_search(arr, start, end, key)
# if index!= -1:
#     print("The value present at: "+str(index))
# else:
#     print("The value is not present in the array!")