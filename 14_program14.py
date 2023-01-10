
# Program to check prime number

number = int(input("Enter a number:"))

if number == 1:
    print(number,"is not the prime number")
if number > 1:
    for i in range(2,number):
        if number%i == 0: 
            print(number,"is not a prime number")
            break
    else:
        print(number,"is the prime number")