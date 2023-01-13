
# armstrong number in an interval

lower = int(input("Enter the lower number:"))
upper = int(input("Enter the upper number:"))

for num in range(lower, upper+1):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        # sum = sum + digit**order 
        cube = digit**order
        sum = sum + cube
        temp = temp//10

    if sum == num:
        print(sum)

