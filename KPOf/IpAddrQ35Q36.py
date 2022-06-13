#Time complexity is O(N)

#Method 1

def ip_addr(arr):
    d = dict()
    maxipList= []
    for i in arr:
        # indexVal = i.index(" ")
        indexVal=i.find(" ")
        ipAddr = i[:indexVal]
        if ipAddr in d:
            d[ipAddr] += 1
        else:
            d[ipAddr] = 1
    # print(d)
    max_count = max(d.values())
    # print(max_count)
    for key,value in  d.items():
        if value == max_count:
            maxipList.append(key)
        
    return maxipList

arr= ["10.10.10.1 BroXX yyyy ZZZ", "10.10.10.2 BroXXd zzz", "10.10.10.2 ddddd yyy ZZZ", "10.10.10.1 BroXX yyyy ZZZ"]
# arr=["10.10.10.1 BroXX yyyy ZZZ", "10.10.10.2 BroXXd zzz","10.10.10.1 BroXX yyyy ZZZ", "10.10.10.2 BroXXd zzz", "10.10.10.2 ddddd yyy ZZZ", "10.10.10.1 BroXX yyyy ZZZ"]
res = ip_addr(arr)
print(res)



# Method2

# def ip_addr(arr):
#     d = dict()
#     max_count = 0
#     max_ip= []
#     for i in arr:
#         indexVal = i.index(" ")
#         ipAddr = i[:indexVal]
#         if ipAddr in d:
#             d[ipAddr] += 1
#             if d[ipAddr] > max_count:
#                 max_count = d[ipAddr]
#         else:
#             d[ipAddr] = 1
#     valmax = max(zip(d.values(), d.keys()))[0]
#     keymax = max(zip(d.values(), d.keys()))[1]
#     res=[]
#     for i in range(valmax):
#         res.append(keymax)
#     return res
    

# arr= ["10.10.10.1 BroXX yyyy ZZZ", "10.10.10.2 BroXXd zzz", "10.10.10.2 ddddd yyy ZZZ", "10.10.10.1 BroXX yyyy ZZZ"]
# res = ip_addr(arr)
# print(res)


#Method 3
# def ip_addr(arr):
#     d = dict()
    
#     countExist =0
#     for i in arr:
#         indexVal = i.index(" ")
#         ip = i[:indexVal]
#         countFirst = 1
#         if ip not in d:
#             d[ip] = countFirst + 1
#         else:
#             d[ip] = countExist +1
#             countExist +=1
#     # print(d)
#     #Another way of returning
#     # for key, values in d.items():
#     #     fin_max = max(d, key=d.get)
#     # return fin_max
#     v = list(d.values())
#     k = list(d.keys())
#     print(d,v,k)
#     resIP = k[v.index(max(v))]
        
#     return resIP

# arr= ["10.10.10.1 BroXX yyyy ZZZ", "10.10.10.1 BroXXd zzz", "10.10.10.2 ddddd yyy ZZZ", "10.10.10.2 ddddd yyy ZZZ", "10.10.10.2 ddddd yyy ZZZ", "10.10.10.1 BroXX yyyy ZZZ", "10.10.10.1 BroXX dsf ZZZ"]
# res = ip_addr(arr)
# print(res)


#Method 3 without using max in dictionaries

# def ip_addr(arr):
#     d = dict()
#     maxipList= []
#     for i in arr:
#         indexVal = i.index(" ")
#         ipAddr = i[:indexVal]
#         if ipAddr in d:
#             d[ipAddr] += 1
#         else:
#             d[ipAddr] = 1
#     # print(d)

#     max_count = 0
#     for i in d.values():
#         if max_count< i:
#             max_count = i
#     print(max_count)
#     for key,value in  d.items():
#         if value == max_count:
#             maxipList.append(key)
        
#     return maxipList

# arr= ["10.10.10.1 BroXX yyyy ZZZ", "10.10.10.2 BroXXd zzz","10.10.10.1 BroXX yyyy ZZZ"]
# res = ip_addr(arr)
# print(res)