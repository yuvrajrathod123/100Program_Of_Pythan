
# program to find number divisible by another number using for loop

# n = int(input("Enter a number: "))
# print("the numbers divisible by",n,"in range 1 to 100")

# for i in range(1,100):
#     if i % n == 0:
#         print(i)


# program to find number divisible by another number using list

l = [26,39,33,45,65,91,78,45]

result = list(filter(lambda x : x % 13 == 0,l))

print("The number divisible by 13 are:",result)

