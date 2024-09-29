# Python 3 code to compute
# average of two numbers
# import sys
# from math import floor

# INT_MAX = 2147483647

# # Function to compute
# # average of two numbers
# def compute_average(a, b):
# 	return floor((a + b) / 2)

# # Driver code
# if __name__ == '__main__':
	
# 	# Assigning maximum integer value
# 	a = INT_MAX
# 	b = -INT_MAX - 1

# 	# Average of two equal numbers
# 	# is the same number
# 	print("Actual average : ", INT_MAX)

# 	# Function to get the
# 	# average of 2 numbers
# 	print("Computed average : ",
# 		compute_average(a, b))


# Improved Formula that does not cause overflow : 
# Average = (a // 2) + (b // 2) + ((a % 2 + b % 2) // 2)
# Below is the implementation :

# Python code to compute
# average of two numbers
INT_MAX=2147483647

# Function to compute
# average of two numbers
def compute_average(a,b):

	return (a // 2) + (b // 2) + ((a % 2 + b % 2) // 2)

# Driver code
if __name__ =="__main__":
	# Assigning maximum integer value
	a = INT_MAX
	b = INT_MAX

	# Average of two equal
	# numbers is the same number
	print( "Actual average : ",INT_MAX)

	# Function to get the
	# average of 2 numbers
	print( "Computed average : ",
			compute_average(a, b))
