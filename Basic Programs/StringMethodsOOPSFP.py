
def stringmethod(para, special1, special2, list1, strfind):
    # Write your code here
    a=para
    b=special1
    for char in b:
        a=a.replace(char,"")
    word1=a
    rword2=word1[69::-1]
    print(rword2)
    rword2=rword2.replace(" ","")
    print(rword2)
    k=",".join(rword2)
    print(k)
    elp=[]
    elpe=[]
    for el in list1:
        if(el in para):
            elp.append(el)
            p=True
        else:
            elpe.append(el)
            p=False
    if(p is True):
        print("Every string in {} were present".format(elp))
    else:
        print("Every string in {} were not present".format(elpe))
    sp=word1.split(" ")
    print(sp[:20])
    unique=set(sp)
    fl=[]
    for i in unique:
        f=sp.count(i)
        fl.append(f)
    print(fl)
      
    

    
if __name__ == '__main__':
    para = input()

    spch1 = input()

    spch2 = input()
    
    qw1_count = int(input().strip())

    qw1 = []

    for _ in range(qw1_count):
        qw1_item = input()
        qw1.append(qw1_item)

    strf = input()

    stringmethod(para, spch1, spch2, qw1, strf)
	
	
	
	
	
	'''
	# Write your code here
    a=para
    b=special1
    for char in b:
            a=a.replace(char,"")
    word1=a
    rword2=word1[69::-1]
    print(rword2)
    for i in rword2:
        rword2=rword2.replace(" ","")
    jstring=special2.join(rword2)
    print(jstring)
    ele=[]
    elep=[]
    p=False
    for i in list1:
        if i in para:
            ele.append(i)
            p=True
        else:
            elep.append(i)
            p=False
    if(p is True):
        print("Every string in {} were present".format(ele))
    else:
        print("Every string in {} were not present".format(elep))
    sp=word1.split(" ")
    print(sp[:20])
    '''
	
	
	'''
	#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'strmethod' function below.
#
# The function accepts following parameters:
#  1. STRING para
#  2. STRING spch1
#  3. STRING spch2
#  4. LIST li1
#  5. STRING strf

def stringmethod(para, special1, special2, list1, strfind):
    # Write your code here
    a=para
    b=special1
    for char in b:
            a=a.replace(char,"")
    word1=a
    rword2=word1[69::-1]
    print(rword2)
    for i in rword2:
        rword2=rword2.replace(" ","")
    jstring=special2.join(rword2)
    print(jstring)
    ele=[]
    elep=[]
    p=False
    for i in list1:
        if i in para:
            ele.append(i)
            p=True
        else:
            elep.append(i)
            p=False
    if(p is True):
        print("Every string in  {} were present".format(ele))
    else:
        print("Every string in  {} were not present".format(elep))
    sp=word1.split(" ")
    print(sp[:20])
    g=[]
    h=[]
    for j in word1.split():
        if j in h:
            pass
        else:
            h.append(j)
    for i in h:
        if h.count(i)<3:
            g.append(i)
    print(g[-20:])
    print(word1.rindex(strfind))
    

if __name__ == '__main__':
