num=int(input())
for i in range(num):
    for k in range(num-i,0,-1):
        print("*",end="")
    for l in range(0,2*i):
        print(" ",end="")
    for m in range(num-i,0,-1):
        print("*",end="")
    print()

for i in range(num):
    for k in range(0,i+1):
        print("*",end="")
    for l in range(num-i-1,0,-1):
        print(" ",end="")
        print(" ",end="")
    for m in range(0,i+1):
        print("*",end="")
    print()

'''
5

**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********

7

**************
******  ******
*****    *****
****      ****
***        ***
**          **
*            *
*            *
**          **
***        ***
****      ****
*****    *****
******  ******
**************

'''