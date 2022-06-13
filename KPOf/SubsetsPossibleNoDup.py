nums = [1,2,2]

#subsets
# templists=[]
# for i in range(len(nums)+1):
#     for j in range(i):
#         templists.append(nums[j:i])
# print(templists)


#Subsets without duplicates
def Sub_Sets(nums):
    temp_lists = [[]]
    d={}
    nums.sort()
    for i in nums:
        start_pos = d.get(i,0)
        value = [j+[i] for j in temp_lists[start_pos:]]
        # print(value)
        temp_lists += value
    # print(temp_lists)
    list2=[]
    for i in temp_lists:
        if i not in list2:
            list2.append(i)
        else:
            continue
    print(list2)
Sub_Sets(nums)