
# python program to make a simple calculator

n1 = float(input("Enter first number:"))
n2 = float(input("Enter second number:"))


print("1.addition")
print("2.substraction")
print("3.multiplication")
print("4.division")
choice = int(input("Enter Your choice:"))

if choice == 1:
    print("The addition of",n1,"and",n2,"is:",n1+n2)    
elif choice == 2:
    print("The substraction of",n1,"and",n2,"is:",n1-n2)
elif choice == 3:
    print("The multiplication of",n1,"and",n2,"is:",n1*n2)
elif choice == 4:
    print("The division of",n1,"and",n2,"is:",n1/n2)
else:
    print("Invalid choice")             