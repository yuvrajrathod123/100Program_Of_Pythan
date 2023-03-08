
class arithmatic:

   
        def getinfo(self):
            self.a = int(input("enter a number:"))
            self.b = int(input("enter second number:"))

        def calculation(self):
             
            while(1):
                print("1.add\n2.substract\n3.multi\n4.division\n5.quit")
                a = int(input("Enter your choice"))

                if a == 1:  
                    print("additon")
                    add = self.a+ self.b 
                    print(add)  
                if a== 2:
                    print("substracton")
                    sub = self.a- self.b 
                    print(sub)  
                if a== 3:
                    print("multiplication")
                    mult = self.a* self.b
                    print(mult)   
                if a == 4:
                    print("division")
                    add = self.a/ self.b  
                    print(mult)

                if a == 5:
                    exit(0) 



cal1 = arithmatic()
cal1.getinfo()
cal1.calculation()
         