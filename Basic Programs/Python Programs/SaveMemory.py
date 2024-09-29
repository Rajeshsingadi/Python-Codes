import sys

l = [i for i in range(5000)]
print(sum(l))
print(sys.getsizeof(l, "bytes"))


my_gen = (i for i in range(5000))
print(sum(my_gen))
print(sys.getsizeof(my_gen, "bytes"))