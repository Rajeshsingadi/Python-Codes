1)```python
arr = [1,2,3,4]

output = [4,2,3,1]

ans)

def swap(arr):
   length = len(arr)
   if length<2:
   		return arr
   	else:
   		arr[0], arr[-1] = arr[-1],arr[0]
   	return arr
   
   print(swap(arr))
   ```