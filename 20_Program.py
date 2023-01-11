
# to display multiplication of given number

num = int(input("enter a to greate a table of that number:"))

# for i in range(num,num*11,num):
#     print(i)
# OR

# for i in range(1,11):
#    print(num,"x",i,"=",num*i)

i = 0
while i<11:
    print(num*i)
    i = i + 1
    