# 1)
# swapping the variables
# A)
# def swap(a,b):
#     a,b=b,a
#     print(a,b)
# swap(10,16)

# 2)
#merging and soring without inbuilt functions
# a=[1,3,5,7]
# b=[2,4,6,8]

# A)
# Approach 1

# la=len(a)
# lb=len(b)
# i, j = 0, 0
# merge_list = []
# while i < la and j < lb:
#     if a[i] < b[j]:
#         merge_list.append(a[i])
#         i += 1
#     else:
#         merge_list.append(b[j])
#         j += 1

# while i < la:
#     merge_list.append(a[i])
#     i += 1

# while j < lb:
#     merge_list.append(b[j])
#     j += 1

# print(merge_list)

# Time Complexity: O(la + lb)
# Space Complexity: O(la + lb)

# # Approach 2
# k=a+b
# print(k)
# for i in range(len(k)):
#     for j in range(i+1,len(k)):
#         if k[i]>k[j]:
#             temp=k[i]
#             # print(k[i],k[j])
#             k[i]=k[j]
#             k[j]=temp
            
# print(k)

# Time Complexity: O((la + lb)²) (slower due to quadratic complexity from bubble sort)
# Space Complexity: O(la + lb)

# 3)
#count the variables in the string
# s=input()
# d={}
# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i] = 1
# print(d) 

# 4)
s="up 1/1/1 to 1/1/44"
max_val = s[s.rfind("/")+1:]
# print(max_val)

StringIntialValue = s[s.find("up")+3:s.find("to")-1]
print(StringIntialValue)

IterInitialValue = StringIntialValue[:StringIntialValue.rfind("/")+1]
# print(IterInitialValue)
result = ""
result_list = []
for i in range(0, int(max_val)):
    temp = IterInitialValue +str(i)
    result = result+temp+","

print(result)