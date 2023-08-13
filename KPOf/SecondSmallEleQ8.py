# second smallest element in the array
#Method 1
# l = [3,7,12,1,1,2]
l=[2,3,1,1,6]
def second_smallest_function(l):
    first_smallest = 1e9
    second_smallest = 1e9
    for num in l:
        if num<first_smallest:
            second_smallest=first_smallest
            first_smallest=num
        if num>first_smallest and num<second_smallest:
            second_smallest=num
    return second_smallest
print(second_smallest_function(l))


#Method 2
# l = [3,7,12,1,1,2]
# def findSmallest(l):
#     small_num=l[0]
#     for i in l:
#         if small_num>i:
#             small_num = i
#     return small_num

# small = findSmallest(l)

# second = l[0]
# for i in range(0,len(l)):
#     if l[i]!=small and second>l[i]:
#         second=l[i]
# print(second)

#Method 2 brute force O(N^2)
# arr = [3,7,12,1,2]
# for i in range(len(arr)):
#     for j in range(i , len(arr)):
#         if arr[i]>arr[j]:
#             temp =arr[i]
#             arr[i] = arr[j]
#             arr[j] = temp
# print(arr[1])

#Method 3
# arr = [3,7,12,1,2]
# arr.sort()
# print(arr[1])