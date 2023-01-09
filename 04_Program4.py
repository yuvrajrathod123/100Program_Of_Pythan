
# Program to solve the quadratic equation (ax**2 + bx + c = 0)
# a, b, c are real number
# a != 0
import cmath

a = float(input("Enter a number a (a!=0):"))
b = float(input("Enter a number b:"))
c = float(input("Enter a number c:"))

# Formula for Discriminant
d = (b**2)-(4*a*c)
root1 = (-b-cmath.sqrt(d))/2*a
root2 = (-b+cmath.sqrt(d))/2*a


print("root1:",root1)
print("root2:",root2)

print(type(root1))
print(type(root2))