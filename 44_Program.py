
#  python program to decimal to binary using recursion

num = int(input("Enter a decimal to be convert into binary: "))
def decimaltobinary(n):
    if n > 1:
        decimaltobinary(n//2)

    print(n%2, end=" ")


decimaltobinary(num)

