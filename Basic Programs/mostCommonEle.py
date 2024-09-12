from collections import Counter

l = [10,10,10,5,5,2,9,9,9,9,9]
counter = Counter(l)
# print(counter)
most_common = counter.most_common(2)
print(most_common[0][0])