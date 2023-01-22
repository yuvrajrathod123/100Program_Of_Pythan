
# program to find number divisible by another number using for loop

n = int(input("Enter a number: "))
print("the numbers divisible by",n,"in range 1 to 100")

for i in range(1,100):
    if i % n == 0:
        print(i)

