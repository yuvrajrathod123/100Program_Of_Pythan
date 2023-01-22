
# program to covert decimal to binary,octal,hexdecimal

decimal = int(input("enter the number here:"))

print("The conversion of decimal number",decimal,"is: ")
print(bin(decimal),"In binary") #0b is prefix for binary
print(oct(decimal),"In octal")  #0o is prefix for octal  
print(hex(decimal),"In hexdecimal")  #0x is prefix for hexa decimal