# program to print the factorial of the number (using for loop)

num = int(input("enter a number:"))

factorial = 1

if factorial < 1:
    print("factorial does not exit")
if num == 0:
    print("factorial of zero is", 1)
if num > 0:
    for i in range(1,num+1):
        factorial = factorial * i
        
print("The factorial of",num,"is",factorial)