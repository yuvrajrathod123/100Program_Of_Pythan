
# To print armstrong number
# 153 is an armstrong number
# 153 = (1x1x1)+(5x5x5)+(3x3x3)
#     =  1 + 125 + 27
#     =  153

# 53 is not an armstrong number
# 53 = (5x5)+(3x3)
#    =  25 + 9
#    =  34

num = int(input("Enter a number:"))
n = int(input("enter the number of digit in the number:"))
sum = 0
temp = num

while temp >  0:
    digit = temp % 10
    cube = digit**n
    sum = sum + cube
    temp = temp//10

print("sum",sum)
if sum == num:
    print("the number is armstrong number")
else:
    print("the number is not the armstrong number")