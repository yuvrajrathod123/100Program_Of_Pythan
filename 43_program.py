
# program to find the factorial number using recursion

n = int(input("Enter a number:"))
def fact(n):
    if n <= 1:
        return n
    else: 
        return fact(n-1)*n

if n<0:
    print("plz enter the positive number")
else:    
    print("factorial of",n,"is:",fact(4))    