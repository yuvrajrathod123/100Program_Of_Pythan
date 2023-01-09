
# program to check leaf year
# year = 365days
# leaf year = 366days

year = int(input("Enter any year:"))

if (year % 400 == 0) and (year % 100 == 0) or (year % 4 == 0) and (year % 100 != 0):
     print(year,"is a leaf year")
# elif (year % 4 == 0) and (year % 100 != 0):
#     print(year,"is a leaf year")
else:
    print(year,"is not the leaf year")