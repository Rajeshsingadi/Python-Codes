# https://www.shiksha.com/online-courses/articles/python-dictionary-practice-programs-for-beginners/

# Check if a Given Key Already Exists in Dictionary
# 1) 
#Creating a Dictionary
D1 = {'first_name' : 'Jim', 'age' : 23, 'height' : 6.0 , 'job' : 'developer', 'company': 'XYZ'}

def check_key(d):
    if d in D1:
        return "Key exists"
    else:
        return "Given key doesn't exist"
    
print(check_key('first_name'))

# 2)
# Handle Missing Keys in Dictionary

print(D1.get('name', 'Not present'))
print(D1.get('first_name',  'Not present'))