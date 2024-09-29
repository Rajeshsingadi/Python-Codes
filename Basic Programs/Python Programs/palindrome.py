string = input("Please give a String : ")
if(string == string[:: - 1]):
   print("Given String is a Palindrome")
else:
   print("Given String is not a Palindrome") 


'''

def isPalindrome(string): 
    for i in range(0, int(len(string)/2)): 
        if string[i] != string[len(string)-i-1]:
            return False
    return True
 
string = input("Please give a String : ")

if (isPalindrome(string)):
    print("Given String is a Palindrome")
else:
    print("Given String is not a Palindrome")

'''



'''
# Program to check if a string is palindrome or not

my_str = 'aIbohPhoBiA'

# make it suitable for caseless comparison
my_str = my_str.casefold()

# reverse the string
rev_str = reversed(my_str)

# check if the string is equal to its reverse
if list(my_str) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")

'''

'''
# Python Program to Check a Given String is Palindrome or Not

string = input("Please enter your own String : ")
str1 = ""

for i in string:
    str1 = i + str1  
print("String in reverse Order :  ", str1)

if(string == str1):
   print("This is a Palindrome String")
else:
   print("This is Not a Palindrome String")
   
'''