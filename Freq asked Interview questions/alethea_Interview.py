# swapping the variables
# def swap(a,b):
#     a,b=b,a
#     print(a,b)
# swap(10,16)

#merging and soring without inbuilt functions
# a=[1,3,5,7]
# b=[2,4,6,8]
# la=len(a)
# lb=len(b)


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

#count the variables in the string
# s=input()
# d={}
# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i] = 1
# print(d) 

s="up 1/1/1 to 1/1/44"
# k=s.split('to')
        
l=[1/1/1, 1/1/2, 1/1/3, 1/1/4]
max_Val = int(s[s.rfind("/")+1:])
# print(max_Val)

stringrep = s[s.find("up")+3:s.find("to")-1]
tempstringrep = stringrep[:stringrep.rfind("/")+1]
result = ""
for i in range(0, max_Val):
    temp = tempstringrep
    temp = temp + str(i)
    # print(temp)
    result = result+temp+","
    
print(result)
    