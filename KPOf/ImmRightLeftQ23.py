def findElement(nums):
    l = len(nums)
    if l<=1:
        return 0
    lmin = 0
    if nums[0]<nums[1]:
        lmin = nums[0]
        return lmin
    elif nums[-1]< nums[-2]:
        lmin = nums[-1]
        return lmin
    else:
        for i in range(1, l-1):
            if  nums[i] < nums[i-1] and nums[i] < nums[i+1]:
                lmin = nums[i]
                return lmin

# arr=[10,8,7,-1,6,9]
# arr= [-4,-6,3,1,4]
arr=  [1,2,3,4,5,6,8]
print(findElement(arr))
