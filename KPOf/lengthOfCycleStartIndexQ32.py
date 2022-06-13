'''
Given an integer array of size n. Elements of the array is >= 0. Starting from arr[startInd], follow each element to the index it points to. Find a cycle and return its length. No cycle is found -> -1.

int lengthOfCycle(int[] arr, int startIndex) {
	// todo
}
Examples:

lengthOfCycle([1, 0], 0); // 2
lengthOfCycle([1, 2, 0], 0); // 3
lengthOfCycle([1, 2, 3, 1], 0); // 3

'''

def lengthOfCycle(arr, startIndex):
    n= len(arr)
    if startIndex<0 or startIndex>=n: return -1
    slow, fast = arr[startIndex], arr[startIndex]
    if not (slow<n and fast<n and arr[fast] < n): return -1
    count = 0
    while slow<n and fast<n and arr[fast]<n:
        slow = arr[slow]
        fast = arr[fast]
        fast = arr[fast]
        count+=1
        if slow == fast: break
    if slow != fast: return -1
    return count

# print(lengthOfCycle([1, 0], 0) == 2)
print(lengthOfCycle([1, 2, 0], 0) == 3)
# print(lengthOfCycle([1, 2, 3, 4, 5, 3], 0) == 3)
# print(lengthOfCycle([1, 2, 0], 0) == 3)
# print(lengthOfCycle([1, 2, 3, 1], 0) == 3)
# print(lengthOfCycle([1, 2, 3, 4], 0) == -1)
# print(lengthOfCycle([1, 2, 3, 4], -1) == -1)
# print(lengthOfCycle([1, 2, 3, 4], 4) == -1)
# print(lengthOfCycle([2, 3, 4, 0], 0) == -1)
# print(lengthOfCycle([2, 3, 0], 0) == 2)
# print(lengthOfCycle([3,0,1, 2, 1, 1], 0) )

'''
theory behind it 
f: distance travelled by fast
s: distance travelled by slow
f = x + c1l + y
s = x + c2l + y

#Example [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,6]
#x=till 6 then loop starts from 6 to 18 loops again
#s travels one jump and f travels with 2 jumps
#s and f enter the loop of 6 to 18 and meets first time at 13th place so 6 to 12 consider y part
#consider 13 to 18 as z part 
#loop length is l = y + z
#mathematical proof
2s = f
2(x + c2l + y) = x + c1l + y
2x + 2(c2l) + 2y = x + c1l + y
2x + 2(c2l) + 2y - x - y =  c1l 
2x + 2y - x - y =  c1l - 2(c2l) 
x + y = ( c1 - 2(c2) )l
x  = ( c1 - 2(c2) )l - y
x  = ( c1 - 2(c2) - 1)l + l - y #add -l and +l it will cancel l
x = c3l + l - y # c3=( c1 - 2(c2) - 1)
x = c3l + y + z - y  #Replace second l with y + z as the loop length mentioned at the start
x = c3l + z

'''