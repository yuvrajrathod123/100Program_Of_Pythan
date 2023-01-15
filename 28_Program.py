
# program to add the element in the list using for loop

list = []
n = int(input("enter the size of list:"))
for i in range(n):
    a = input("enter the element:")
    list.extend(a)

print("Newly created list: ",list)