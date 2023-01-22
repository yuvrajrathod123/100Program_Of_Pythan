
# program to find factors of a number

n = int(input("enter a number:"))

print("Fcators of",n,"is:")
for i in range(1,n+1):
    if n %  i == 0:
        print(i)