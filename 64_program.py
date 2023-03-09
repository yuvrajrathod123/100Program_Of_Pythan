
# program to count the each no of vowels using list and dictionary compression

a = input("Enter the string")

vowels = "aeiou"

a = a.casefold()  # casefold convert the capital letter to smalle letter same as lower()
print(a)

count = {key:sum([1 for char in a if char == key]) for key in vowels}

print(count)