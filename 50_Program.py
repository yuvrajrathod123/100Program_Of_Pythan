
#  program to check the number is palindrome or not

num  = int(input("Enter a number"))
temp = num
rev =  0

while num > 0:
    dig = num % 10
    rev = rev*10+dig
    num = num // 10

if temp == rev:
    print("palindrome")
else:
    print("not palindrome")        


# revese the string using list
# my_str = input("Enter a string:")

# my_str = my_str.casefold()

# re_str = list(reversed(my_str))

# print(re_str)