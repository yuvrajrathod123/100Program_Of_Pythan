
# ******
# *****
# ****
# ***
# **
# *

n = int(input("Enter the no of row:"))

for i  in range(1,n):
    for j in range(n, i, -1):
        print("*",end="")
    print()