def minimumFlips(series):
    count1, count2 =0, 0
    for i in range(len(series)):
        if series[i] == "H" and i%2 != 0:
            count1 += 1
        elif series[i] == "T" and i%2 == 0:
            count1 += 1
    for i in range(len(series)):
        if series[i] == "T" and i%2 != 0:
            count2 += 1
        elif series[i] == "H" and i%2 == 0:
            count2 += 1
    return min(count1, count2)
# series = "TTTHTHTHHH"
series = "HTHTHTHTTTH"
res=minimumFlips(series)
print(res)


# def flip(ch):
#     return 'H' if (ch=='T') else 'T'

# def getFlipwithStartingCharcter(str, expected):

#     flipcount = 0
#     for i in range(len( str)):

#         if (str[i] !=expected):
#             flipcount += 1

#     expected = flip(expected)
#     return flipcount

# def minFlipToMakeStringAlternate(str):

#     return min(getFlipwithStartingCharcter(str,'T'), getFlipwithStartingCharcter(str, 'H'))

# if __name__== "__main__":

#     s = "TTTHTHTHHH"
#     # s="HTHTTT"
#     print(minFlipToMakeStringAlternate(s))


