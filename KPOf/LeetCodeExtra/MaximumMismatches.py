'''
#Maximum Mismatches

s="abab"
find all possible permutations and reverse(s) == baba-->Maximum Number of Mismatches=4

'''

import itertools
def maximum_mismatches(s,n):
    if len(set(s))==1:
        return 0
    
    max_c=0
    for str_c in set(itertools.permutations(s,n)):
        rev_str = str_c[::-1]
        counter=0
        for i in range(n):
            if str_c[i]!= rev_str[i]:
                counter += 1
        max_c = max(max_c, counter)
        # (another way)
        # if max_c < counter:
        #     max_c = counter
    
    return max_c

# s="aatacanaa"-->6
s="abab"
n=len(s)
print(maximum_mismatches(s,n))

'''
question at :
https://leetcode.com/discuss/interview-question/703529/Programming-Question-Goldmann-Sachs
image.png
https://assets.leetcode.com/users/images/b03a3449-1937-4fb9-82b6-0921cc378b6f_1593010484.8493035.png
https://assets.leetcode.com/users/images/607c737c-37da-43f0-8fde-336f8cf00f51_1593010489.675383.png
'''