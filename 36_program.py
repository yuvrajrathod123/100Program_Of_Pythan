
# program to find the hcf(hight common factor) or gcd (gratest comm divisior)

def calHCF(x,y):
        if x > y:
            smaller = y
        else:
            smaller = x

        for i in range(1,smaller+1): 
            if(x%i == 0) and (y%i== 0):
                HCF = i 
                           
        print("HCF for the",x,"and",y,"is",HCF)

n1 = int(input("enter first no:"))
n2 = int(input("enter seconf no:"))
calHCF(n1,n2)            