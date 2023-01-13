
# program to print the the sum of first n natural number

num = int(input("enter a number here: "))

if num < 0:
    print("Please enter the positive number: ")
else:
    sum = 0
    while num >0:
        sum += num
        num -= 1

    print("the sum of the first n natural numbers is",sum)     