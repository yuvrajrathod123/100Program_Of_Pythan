
# program to count the number of Vowel in a string

a = {'a','e','i','o','u','A','E','I','O','U'}

string = input("Enter a string: ")
count = 0
for i in string:
    if i in a:
        count = count + 1


print("Number of vowels in string is :",count)
