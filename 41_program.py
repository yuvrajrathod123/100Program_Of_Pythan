
# Display fibonacci sequency using recursion (0 1 1 2 3 5 8 13)

n = int(input("print first n term of fibonacci series:"))

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

if n<=0:
    print("Plz enter the positive number:")
else:    
    print("Fibonacci series is:", end=" ")
    for i in range(0,n):
        print(fib(i), end=" ")


