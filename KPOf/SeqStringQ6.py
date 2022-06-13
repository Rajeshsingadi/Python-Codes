
#Method 1 with lists
s="abcde"
step=3
def generateSeq(s, step):
    length = len(s)
    res = [s[i:i+step] for i in range(len(s))]
    newRes = []
    for i in res:
        if len(i)!=step:
            res.remove(i)
        else:
            newRes.append(i)
    return(newRes)
print(generateSeq(s,step))

#Method 2 with sets

# def sequenceString(mystr, step):
#     check = step
#     s = set()
#     for i in range(len(mystr)):
#         if len(mystr[i:check]) == step:
#             s.add(mystr[i:check])
#             check += 1
#     return s

# mystr="abcde"
# step = 3
# res = sequenceString(mystr, step)
# print(res)