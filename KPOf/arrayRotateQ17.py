def arrayRotation(arr,rotate):
    n=len(arr)
    first_arr = []
    second_arr = []
    check = 0
    while rotate>n:
            rotate -= n
                
    while check < rotate:
        first_arr.append(arr[check])
        check += 1
    while rotate < n:
        second_arr.append(arr[rotate])
        rotate += 1
        
    if sum(first_arr) > sum(second_arr):
        return "the first array has the greater sum: " + str(int(sum(first_arr)))
    else:
        return "the second array has the greater sum: " + str( int(sum(second_arr)))
    

arr= [1,2,3,4]
rotate = 10
res =arrayRotation(arr, rotate)
print(res)