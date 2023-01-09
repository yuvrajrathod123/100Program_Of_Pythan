
# Python program to check if a number is positive, negative or 0

num = int(input("Enter a number(- or + or 0):"))

if num > 0:
    print(num,"is a positive number")
elif num < 0:
    print(num,"is a negative number")
else:
    print("number is zero")

