

#     *
#    * *
#   * * *
#  * * * *
# * * * * *

n = int(input("Enter the no of rows:"))

for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(end=" ")
    for l in range(1,i+1):
        print("*",end=" ")  
    print()