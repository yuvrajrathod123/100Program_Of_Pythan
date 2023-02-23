
# python program to sort the word in alphabetical order


a = input("Ente a string:")

w = a.split()  # split is used to seprate the word as an element of staring

for i in range(len(w)):
    w[i] = w[i].lower()   # lower is used to convert capital letter to small
                          # if we dont make the letter small then the sort function first sort the capital letter after that it will sort the small letter

print(w)
print()
w.sort()   # it will sort the word by alphabetical order
print()
print(w)
print()

for r in w:
    print(r)