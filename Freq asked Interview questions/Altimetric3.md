1)
emp_data :
 
emp_id mob_no   Address	        Flag

 123	 7777777	 Bangalore		Y

 456   8888888	 Chennai		     Y

 789   9999999	 Pune			Y

 124   6666666	 Hyderabad		Y

 333   9199191	 Delhi			Y
 
emp_latest :  
 
emp_id mob_no   Address

 789   9999999   Bangalore

 124   6666666   Hyderabad

 333   9199191   Bangalore

 444   7171717   Jaipur
 
 
Output :
 
emp_id  mob_no  Address           Flag

 123   7777777   Bangalore          Y

 456   8888888   Chennai            Y

 789   9999999   Pune               N

 124   6666666   Hyderabad          Y

 333   9199191   Delhi              N

 444   7171717   Jaipur             Y

 789   9999999   Bangalore          Y

 333   9199191   Bangalore          Y
```
SQL
A)

SELECT 
    e.emp_id, 
    e.mob_no, 
    e.Address, 
    CASE 
        WHEN e.Address != l.Address THEN 'N'
        ELSE e.Flag
    END AS Flag
FROM emp_data e
LEFT JOIN emp_latest l ON e.emp_id = l.emp_id

UNION ALL

SELECT 
    l.emp_id, 
    l.mob_no, 
    l.Address, 
    'Y' AS Flag
FROM emp_latest l
LEFT JOIN emp_data e ON l.emp_id = e.emp_id
WHERE e.emp_id IS NULL;

emp_id  mob_no     Address      Flag
------------------------------------
123     7777777    Bangalore    Y
456     8888888    Chennai      Y
789     9999999    Pune         N
124     6666666    Hyderabad    Y
333     9199191    Delhi        N
444     7171717    Jaipur       Y
789     9999999    Bangalore    Y
333     9199191    Bangalore    Y


2) 

 
 
 str_val = "Sample"
 
 op  = "maSelp"
 
 odd left string part is taking the highest value give me a python code? 
actually question is divide the string Sam and elp and reverse the both the strings and if it's even join first half with reversed as maS and second half reversed with help so it would be maSelp but if it Is odd length make sure the first half has more length than second half that extra char will be a part of first half Samlple output would be lmaSelp 

 A)  
def rearrange_string(str_val):
    # Calculate the split point
    mid = (len(str_val) + 1) // 2  # First half gets more characters if odd
    
    # Split the string into two parts
    first_half = str_val[:mid]
    second_half = str_val[mid:]
    
    # Reverse both halves
    reversed_first_half = first_half[::-1]
    reversed_second_half = second_half[::-1]
    
    # Concatenate the reversed halves
    result = reversed_first_half + reversed_second_half
    return result

# Example usage
str_val = "Sample"
output = rearrange_string(str_val)
print(output)  # Output: "maSelp"

str_val_odd = "Samlple"
output_odd = rearrange_string(str_val_odd)
print(output_odd)  # Output: "lmaSelp"
