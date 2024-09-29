list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))


def common_elements(list1, list2):
    count1 = 0
    count2 = 0
    result = []
    while count1 < len(list1) and count2 < len(list2):
        if list1[count1] == list2[count2]:
            result.append(list1[count1])
            count1 += 1
            count2 += 1
        elif list1[count1] > list2[count2]:
            count2 += 1
        else:
            count1 += 1

    return result


print(common_elements(list1, list2))

'''
# NOTE: The following input values will be used for testing your solution.
list_a1 = [1, 3, 4, 6, 7, 9]
list_a2 = [1, 2, 4, 5, 9, 10]
# common_elements(list_a1, list_a2) should return [1, 4, 9] (a list).

list_b1 = [1, 2, 9, 10, 11, 12]
list_b2 = [0, 1, 2, 3, 4, 5, 8, 9, 10, 12, 14, 15]
# common_elements(list_b1, list_b2) should return [1, 2, 9, 10, 12] (a list).

list_c1 = [0, 1, 2, 3, 4, 5]
list_c2 = [6, 7, 8, 9, 10, 11]
# common_elements(list_b1, list_b2) should return [] (an empty list).
'''
