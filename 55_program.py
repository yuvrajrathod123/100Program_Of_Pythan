
class shape:
     
     def getinfotri(self):
          self.length = int(input("enter te length of triangle:"))
          self.breath = int(input("enter te breath of triangle:"))
          self.c = int(input("enter the side c of triangle:"))
          self.b = int(input("enter te side b of triangle:"))
          

     def displayinfotri(self):
            area = 1/2*self.length*self.breath
            print("area of trainagle:",area)

            perimeter = self.breath+self.c+self.b
            print("Area of triangle",perimeter)

     def getinforec(self):
          self.length = int(input("enter te length of triangle:"))
          self.breath = int(input("enter te breath of triangle:"))
        #   self.c = int(input("enter the side c of triangle:"))
        #   self.b = int(input("enter te side b of triangle:"))
          

     def displayinforec(self):
            area = self.length*self.breath
            print("area of rectangle:",area)

            perimeter = self.breath+self.breath
            print("Perimeter of rectangle",perimeter)        

            

shape1 = shape()
shape1.getinfotri()
shape1.displayinfotri()

shape2 = shape()
shape2.getinforec()
shape2.displayinforec()
        