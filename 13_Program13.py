
# Program to find the largest number among three number

a = float(input("Enter first number:"))
b = float(input("Enter second number:"))
c = float(input("Enter third number:"))

if a>b and a>c :
    print(a,"is a gretest")
elif b>c and b>a:
    print(b,"is a gretest nummber")
else:
    print(c,"is a gretest number")
    