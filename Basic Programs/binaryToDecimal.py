#print(oct(100)[2:])
num=int(input())
dval=0
i=0
while(num!=0):
    rem=num%10
    dval=dval+rem*pow(2,i)
    num=num//10
    i=i+1
print(abs(dval))
'''
binary
'''

