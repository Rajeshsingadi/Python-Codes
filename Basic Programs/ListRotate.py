# Number of test cases
for test_case in range(int(input())):
    
    # Read input and split into two integers
    size, num_rotations = map(int, input().split())
    
    # Read the list of elements and take only the first 'size' elements
    elements = list(input().split())[:size]
    
    # Calculate the number of effective rotations needed
    effective_rotations = num_rotations % len(elements)
    
    # Calculate the split point for the rotation
    split_point = len(elements) - effective_rotations
    
    # Perform the rotation by splitting and rearranging the list
    rotated_list = elements[split_point:] + elements[:split_point]
    
    # Print the rotated list as a space-separated string
    print(' '.join(rotated_list))


'''
Here are a few sample inputs and their corresponding expected outputs to test the code:

### Sample Input 1:
```
1
5 2
1 2 3 4 5
```

### Expected Output 1:
```
4 5 1 2 3
```

### Explanation:
- You have 5 elements: `1 2 3 4 5`.
- You need to rotate the list by 2 positions.
- The result after 2 right rotations is: `4 5 1 2 3`.

---

### Sample Input 2:
```
2
6 3
10 20 30 40 50 60
4 8
1 2 3 4
```

### Expected Output 2:
```
40 50 60 10 20 30
1 2 3 4
```

### Explanation:
- **First test case:** You have 6 elements: `10 20 30 40 50 60` and rotate by 3 positions, giving: `40 50 60 10 20 30`.
- **Second test case:** You have 4 elements: `1 2 3 4`, rotating by 8 is the same as rotating by 0 because 8 is a multiple of 4, so the result is `1 2 3 4`.

---

### Sample Input 3:
```
1
7 5
a b c d e f g
```

### Expected Output 3:
```
c d e f g a b
```

### Explanation:
- You have 7 elements: `a b c d e f g`.
- Rotate by 5 positions, resulting in: `c d e f g a b`.

This will help you verify that the rotation logic and input parsing are correct.

'''

