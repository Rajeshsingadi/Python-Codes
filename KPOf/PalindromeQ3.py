name = "SOOS"
#Method 1
reverse_name = name[::-1]
if name == reverse_name:
    print("Palindrome")
else:
    print("Not Palindrome")

#Method  2
# name = "SOOS"

# reverse_name = list(reversed(name))
# currentName = list(name)
# if currentName == reverse_name:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

#Method 3
# for i in range(0, int(len(name)/2)):
#     if name[i] == name[len(name)-i-1]:
#         print("Palindrome")
#     else:
#         print("Not Palindrome")

#Method 4 Caseless Matching
# name1 = "SOPpos"
# string = name1.casefold()
# if string == string[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

#Method 5
# s = ""
# for i in name:
#     s = i + s
# if name == s:
#     print("Palindrome")
# else:
#     print("Not Palindrome") 

# name = "SOOS"
# # Method 6
# reverse_name = list(reversed(name))
# name_list=[]
# for i in name:
#     name_list.append(i)
# if name_list == reverse_name:
#     print("Palindrome")
# else:
#     print("Not Palindrome")
