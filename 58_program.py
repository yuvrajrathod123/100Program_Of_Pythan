
class name:

    def getinfo(self):
        self.a = complex(input("Enter the number"))
        self.b = complex(input("Enter the second number"))

    def show(self):
        # print("additon of two complex number")
        add = self.a + self.b
        print("addition of two commplex numbere:",add)

obj1 = name()
obj1.getinfo()
obj1.show()

