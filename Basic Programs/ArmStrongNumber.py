 
num = int(input("Enter any number: "))

temp = num
sum=0

while temp>0:
    rem=temp%10
    sum += rem**3
    temp = temp//10
print(sum)
if num==sum:
    print("Arm Strong number")
else:
    print("Not ARM strong")