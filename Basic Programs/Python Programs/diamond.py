num=int(input())

for i in range(0,num):
    for j in range(0,num-i-1):
        print(" ",end="")
    for k in range(0,i+1):
        print("*", end="")
    for l in range(0,i):
        print("*",end="")
    print()

for i in range(0,num):
    for j in range(0,i+1):
        print(" ",end="")
    for k in range(num-i,1,-1):
        print("*",end="")
    for l in range(num-i-1,1,-1):
        print("*",end="")
    print()

'''
5
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *

10
         *
        ***
       *****
      *******
     *********
    ***********
   *************
  ***************
 *****************
*******************
 *****************
  ***************
   *************
    ***********
     *********
      *******
       *****
        ***
         *
'''


'''
for upper half another logic code

for i in range(0,num+1):
    for j in range(0,num-i):
        print(" ",end="")
    for k in range(0,2*i-1):
        print("*", end="")
    print()

5
     
    *
   ***
  *****
 *******
*********

'''

'''
using functions

def Diamond(rows): 
    n = 0
    for i in range(1, rows + 1): 
        # loop to print spaces 
        for j in range (1, (rows - i) + 1): 
            print(end = " ") 
          
        # loop to print star 
        while n != (2 * i - 1): 
            print("*", end = "") 
            n = n + 1
        n = 0
          
        # line break 
        print()  
  
    k = 1
    n = 1
    for i in range(1, rows): 
        # loop to print spaces 
        for j in range (1, k + 1): 
            print(end = " ") 
        k = k + 1
          
        # loop to print star 
        while n <= (2 * (rows - i) - 1): 
            print("*", end = "") 
            n = n + 1
        n = 1
        print() 
  
# Driver Code 
# number of rows input 
rows = int(input())
Diamond(rows)
'''

'''
5
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *

10
         *
        ***
       *****
      *******
     *********
    ***********
   *************
  ***************
 *****************
*******************
 *****************
  ***************
   *************
    ***********
     *********
      *******
       *****
        ***
         *
'''