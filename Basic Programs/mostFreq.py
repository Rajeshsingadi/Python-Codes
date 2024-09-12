arr = list(map(int, input().split()))


def max_item(arr):
    Dict = {}
    max_count = -1
    max_num = None
    for num in arr:
        if num not in Dict:
            Dict[num] = 1
        else:
            Dict[num] += 1

        if Dict[num] > max_count:
            max_count = Dict[num]
            max_num = num
    return max_num


print(max_item(arr))

# big(o) notation is o(n)

'''
# NOTE: The following input values will be used for testing your solution.
# most_frequent(list1) should return 1.
list1 = [1, 3, 1, 3, 2, 1]
# most_frequent(list2) should return 3.
list2 = [3, 3, 1, 3, 2, 1]
# most_frequent(list3) should return None.
list3 = []
# most_frequent(list4) should return 0.
list4 = [0]
# most_frequent(list5) should return -1.
list5 = [0, -1, 10, 10, -1, 10, -1, -1, -1, 1]
'''
