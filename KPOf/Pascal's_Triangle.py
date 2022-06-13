numRows=6
def pascalTriangle(numRows):
    res=[]
    row=[]
    for i in range(numRows):
        if i==0:
            row=[1]
            res.append(row)
        else:
            row1=[1]
            j=1
            while j<i:
                row1.append(row[j-1]+row[j])
                j+=1
            row1.append(1)
            res.append(row1)
            row=row1
    return res
print(pascalTriangle(numRows))

