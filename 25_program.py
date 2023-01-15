
# program to accept the list and print   the alternate element of list

list = list(input("Enter a list: "))

# list = ['a','b','c','d','e','f'] 
print("original list:", str(list),end=' ')
print()
for i in range(len(list)):
    if i % 2 == 0:
        result = list[i]
        print(str(result),end=' ')
    
