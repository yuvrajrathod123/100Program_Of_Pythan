
# to print fibonacci series

num = int(input("Enter a number:"))

# x = 0
# y = 1

# if num == 1:
#     print(x)
# else:
#     print(x)    
#     print(y)    
#     for i in range(2, num):
#         c = x + y
#         x = y
#         y = c
#         print(c,end=" ")

# OR

x = 0
y = 1

for i in range(1, num + 1):
    c = x + y
    print(x,end=" ")
    x = y
    y = c