
# 1
# 12
# 123
# 1234
# 12345

n = int(input("Enter the number of rows: "))
 
for i in range(1,n):
    for j in range(1,i+1):
        print(j, end=" ")
    print()