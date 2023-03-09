
# inheritance with GET method

class person:

    def __init__(self,first,last):
        self.firstname = first
        self.lasttname = last

    def printName(self):
        name = self.firstname +" " + self.lasttname
        # print("The name of the user is:",name)    

        return name

class employee(person):

    def __init__(self,first,last,staffNumber):
        person.__init__(self,first,last)
        self.staffNumber= staffNumber


    def printinfo(self):
        # a = self.printName() + "," + self.staffNumber
        return self.printName() + "," + self.staffNumber     

x = person("Yuvraj","Rathod")
y = employee("Mayur","Pawar","123")

print(x.printName())
# print(y.printName())
print(y.printinfo())
