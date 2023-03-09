
# program to count the each no of vowels using dictionary

a = input("Enter the string")

vowels = "aeiou"

a = a.casefold()  # casefold convert the capital letter to smalle letter same as lower()
print(a)

count = {}.fromkeys(vowels,0)
print(count)

for char in a:
    if char in count:
        count[char] += 1

print(count)













