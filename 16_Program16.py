
# program to print the factorial of the number (using recursive function)

# n = int(input("Enter a number:"))
# factorial(n)

def factorial(n):
    if  n == 0:
        return 1
    else:
        return n * factorial(n-1)


n = int(input("Enter a number:"))
fact = factorial(n)
print("factorial of",n,"is",fact)
