#Time complexity is O(N)

def maxDiff(a):
    vmin = a[0]
    dmax = 0
    for i in range(len(a)):
        if (a[i] < vmin):
            vmin = a[i]
        elif (a[i] - vmin > dmax):
            dmax = a[i] - vmin
    return dmax
l = [1,2,6,4]
print(maxDiff(l))


#Time complexity is O(N^2)
#  def maxDifference(l):
#     diffList = []
#     for i in range(0,len(l)):
#         for j in range(i+1, len(l)):
#             diffList.append(l[j]-l[i])
#     return max(diffList)
# l = [1,2,6,4]
# res=maxDifference(l)
# print(res)

# def maxDifference(l):
#     res = l[1] - l[0]
#     for i in range(0,len(l)):
#         for j in range(i+1, len(l)):
#             if l[j]-l[i] > res:
#                 res = l[j]- l[i]
#     return res
# l = [1,2,6,4]
# print(maxDifference(l))