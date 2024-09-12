# Input Format

# A single line of input containing the string .

# Constraints
# 3 < len(S) <= 10 ^ 4
# S has at least 3 distinct characters
# Output Format

# Print the three most common characters along with their occurrence count each on a separate line.
# Sort output in descending order of occurrence count.
# If the occurrence count is the same, sort the characters in alphabetical order.

# Sample Input 0

# aabbbccde
# Sample Output 0

# b 3
# a 2
# c 2
# Explanation 0

# aabbbccde
# Here, b occurs 3 times. It is printed first.
# Both a and c occur 2 times. So, a is printed in the second line and c in the third line because a comes before c in the alphabet.

# Note: The string S has at least 3 distinct characters.

#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    s = input()
    Dict = {}
    for i in sorted(s):
        Dict[i] = Dict.get(i, 0)+1
# Sorting Dict by value & storing sorted keys in Dict_keys.
    Dict_keys = sorted(Dict, key=Dict.get, reverse=True)
    for key in Dict_keys[:3]:
        print(key, Dict[key])

# Input (stdin)

# aabbbccde
# Your Output (stdout)
# b 3
# a 2
# c 2
