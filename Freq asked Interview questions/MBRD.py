# 1.string to integer without using int
# s="1234"
# for i in s:
#     print(ord(i)-48)

# 2.
# print(-16%6) 
# output?
# ans->2

# 3.
# output?

# l=[1,2,3,2,3]
# for i in l:
#     if i==2:
#         l.remove(2)
# print(l)

# ans->[1,3,3]

# 4.what are all the joins?inner,left outer,right outer, full outer.
# select s.name,e.salary from employee e inner join students s on s.name=e.name

# 5.demonstrate recursion?plus write codefor HCF?
# def HCF(num1,num2):
#     if num1==0:
#         return num2
#     if num2==0:
#         return num1
#     if num1>num2:
#         return HCF(num1%num2,num2)
#     if num1<num2:
#         # print(num2%num1, num1)
#         return HCF(num1,num2%num1)

# 6.dictionary comprehension
# list1 = [1,2,3,4,5,6]
# list2 = [8,9,0,7]

# output
# 1:8
# 2:9


# print({list1[i]:list2[i] for i in range(len(list1))})

# 7.circular rotation

#  function to rotate array by d elements using temp array
# def rotateArray(arr, n, d):
# 	temp = []
# 	i = 0
# 	while (i < d):
# 		temp.append(arr[i])
# 		i = i + 1
# 	i = 0
# 	while (d < n):
# 		arr[i] = arr[d]
# 		i = i + 1
# 		d = d + 1
# 	arr[:] = arr[: i] + temp
# 	return arr


# # Driver function to test above function
# arr = [1, 2, 3, 4, 5, 6, 7]
# print("Array after left rotation is: ", end=' ')
# print(rotateArray(arr, len(arr), 2))


#ROund 2 L2

# s="{({}[()])()}"
# class Program:
#     def BracketValidator(s):
#         open_list = ['(','{','[']
#         close_list = [')','}',']']
#         stack=[]
#         for i in s:
#             if i in open_list:
#                 stack.append(i)
#             elif i in close_list:
#                 pos = close_list.index(i)
#                 if ((len(stack)>0 and open_list[pos]==stack[len(stack)-1])):
#                     stack.pop()
#                 else:
#                     return "UnBalanced"
#         if len(stack) == 0:
#             return "Balanced"
#         else:
#             return "UnBalanced"
# obj1 = Program.BracketValidator(s)
# print(obj1)

#Median  
s=[1,2,3,10,6,5,7,8]

# 123567810
def Median(s):
    ele=0 
    s.sort() 
    if len(s)%2 !=0:
        ele = s[len(s)//2] 
        return ele
    else:
        mid = len(s)//2 
        ele = (s[mid-1]+ s[mid])/2 
        return ele 
        # print(ele)
print(Median(s))
#Time complexity for each and every row

# import string
# from async_generator import async_generator

# employee

# ID
# employe_firstName,
# last_name,
# age
# salary
# managers_ID

# 1, raj, kumar, 25, 4000, 2, 
# 2, abc, gsh, 26, 5000, 10

# --int
# --string
# --string
# --int
# --float
# --int

# select employee_firstName, Manager_Name from employee where ManagerID = 10

# employee.objects.get(employee_firstName, Manager_Name).filter(manager_id=10)


# student 
# 1. studentID,
# studentclass,
# studentName,
# teacherName
# subject
# attendance_subject
# attendance_Percentage_subject


# l=["flower","flow","flight"]

# class LongestPrefix:
#     def longest_prefix(l):
#         k=1
#         pre=[]
#         all_list=[]
#         for i in l:
#             temp_val = i[:k]
#             pre.append(temp_val)
#             all_list.append(pre)
#             k += 1
#         print(all_list)
#         # return pre[-1]
#         # print(pre)
#         return pre[-1]

# obj = LongestPrefix.longest_prefix(l)
# print(obj)

