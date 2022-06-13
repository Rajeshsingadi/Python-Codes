# st = "apple"
st= "racecars"
def firstNonDup(st):
    dt={}
    res=''
    for i in st:
        if i in dt:
            dt[i] += 1
        else:
            dt[i] = 1

    for i in st:
        if dt[i] == 1:
            # print(i,st.find(i))
            res=i
            return res
print(firstNonDup(st))