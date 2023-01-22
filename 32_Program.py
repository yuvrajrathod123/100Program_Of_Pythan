
# program to display powers of 2 using anonymous function(Lambda function)

nterms = int(input("Enter the no of term:"))

result = list(map(lambda x : 2 ** x, range(nterms+1)))

# print(result)

for i in range(0,nterms+1):
    print("the value of 2 raised to power",i,"is",result[i])