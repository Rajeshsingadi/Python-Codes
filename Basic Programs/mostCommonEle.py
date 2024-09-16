l = [10, 10, 10, 5, 5, 2, 9, 9, 9, 9, 9]
frequency = {}
for num in l:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num]= 1
print(frequency)

max_val = max(frequency, key=frequency.get)

print("Maximum number of times that is repeated in the list is : ", max_val)

print("Number of times the maximum value is repeated is: ", frequency[max_val])

'''
Time Complexity:
Building the frequency dictionary: O(n), where n is the length of the list l.
Finding the maximum: max() iterates over all k elements in the dictionary (where k is the number of unique elements). The key=frequency.get ensures that the maximum is found based on the value (frequency).
This step takes O(k) time.
In the worst case, k = n.
Total time complexity: O(n) + O(k) ≈ O(n) in the worst case.

Space Complexity:
Dictionary: O(k), where k is the number of unique elements in the list.
Total space complexity: O(k), which is O(n) in the worst case when all elements are distinct.

'''