def FirstDuplicateElementInString(S):
    h = {} #Empty Hash table
    for i in S:
        if i in h:
            return i
        else:
            h[i] = 0
    return 0

S = input()
print(FirstDuplicateElementInString(S))