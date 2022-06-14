#Q28

from itertools import permutations

def extractTime(nums):
    n = len(nums)
    if n>4:
        return 0
    else:
        for i in permutations(sorted(nums, reverse=True)):
            if i[:2] < (2,4) and i[2] < 6:
                return "%d%d:%d%d" % i
        return -1

# nums = [1,2,3,4]
nums = [2,6,1,3]
print(extractTime(nums))


'''
#Q38
def timestamp(l):
    for part in l:
        if part>2: continue
        for part1 in l:
            if part == part1: continue
            elif part==2 and part1>3: continue
            else: hr.append(str(part)+str(part1))
    print(hr)

    for part in l:
        if part>6: continue
        for part1 in l:
            if part == part1: continue
            elif part ==6 and part1>0: continue
            else: mn.append(str(part)+str(part1))

    print(mn)

    for i in hr:
        for j in mn:
            if i==j:
                continue
            else:
                hh_mm.append(str(i)+":"+str(j))

    # print(hh_mm)
    return hh_mm

hr = []
mn=[]
hh_mm =[]
l=[1,2,3,4,5,6,7,8,9]
print(timestamp(l))
'''