
# program to convert tuple into list and vice versa

t1 = tuple(input("enter a tuple to convert it into list:"))
print("current tuple:",t1)
l1 = list(t1)

print("the corresponding list:",l1)

print()

l2 = list(input("enter the lis to convert it into tuple:"))
print("current list:",l2)
t2 = tuple(l2)

print("the corresponding list:",t2)
