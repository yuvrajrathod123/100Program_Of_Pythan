
# program to check the string id palindrome or not

a =  input("Enter a string")

rev = a[::-1]   

if a == rev:
    print("palindrome")
else:
    print("not")   
