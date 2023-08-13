#list sorting without the in-built functions
#ascending order

#using the in-built function
l=[3,2,6,4]
l.sort
print(l)

#list reverse
print(l[::-1])

#Time complexity O(N)
# l=[3,2,6,4]
# new_list =[]
# while l:
#     minimum = l[0]
#     for i in l:
#         if i < minimum:
#             minimum = i
#     new_list.append(minimum)
#     l.remove(minimum)
# print(new_list)



#list reverse using traditional method
# for i in range(len(l)):
#     for j in range(i+1, len(l)):
#         if l[i]<l[j]:
#             temp=l[j]
#             l[j]=l[i]
#             l[i]=temp
# print(l)


#Time complexity O(N^2)
# l=[3,2,6,4]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]>l[j]:
#             temp=l[i]
#             l[i]=l[j]
#             l[j]=temp
# print(l)

'''
The time complexity of sorting an array in O(N) is not possible using comparison-based sorting algorithms like QuickSort or MergeSort, which have an average time complexity of O(N log N). However, if you have certain constraints or additional information about the data, you might be able to achieve linear time complexity.

One such scenario is when you have prior knowledge about the range of values in the array. In this case, you can use a counting sort algorithm, which can achieve O(N) time complexity.

Here's an example of how you could implement counting sort in Python'''
def counting_sort(arr):
    # Find the maximum and minimum values in the array
    max_val = max(arr)
    min_val = min(arr)

    # Calculate the range of values
    range_of_values = max_val - min_val + 1

    # Create a counting array to store the count of each element
    count_array = [0] * range_of_values

    # Count the occurrences of each element
    for num in arr:
        count_array[num - min_val] += 1

    # Reconstruct the sorted array
    sorted_array = []
    for i, count in enumerate(count_array):
        sorted_array.extend([i + min_val] * count)

    return sorted_array

# Example usage
input_array = [4, 2, 2, 8, 3, 3, 1]
sorted_array = counting_sort(input_array)
print(sorted_array)
