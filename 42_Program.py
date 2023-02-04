
# python program to find the sum of natural numbers using recursion


n = int(input("Enter a number:"))
def sum(n):
    if n <= 1:
        return n
    else:
        return sum(n-1)+ n

if n<0:
    print("plz enter the positive number:")
else:
    print("The sum  of natural upto given number is:", sum(n))
    # for i in range(0,n+1):
    #     x = sum(i)

    # print(x)

