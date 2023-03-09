
# Method overloading

class shape:

    def __init__(self,length):
        self.length = length

    def area(self):
        area = self.length *self.length
        print("Area of square:",area)    

class rectangle:
     def __init__(self,length,breath):
        self.length = length
        self.breath = breath

     def area(self):
        area = self.length *self.breath
        print("Area of square:",area)    
    

length = float(input("Enter te the length"))
breath = float(input("Enter te the brath"))

obj1 = rectangle(length,breath)
obj1.area()

obj2 = shape(length)
obj2.area()