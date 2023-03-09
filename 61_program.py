
# inheritance with __str__(self) and super method

class person:

    def __init__(self,first,last,age):
        self.firstname = first
        self.lasttname = last
        self.age = age

    def __str__(self):
        name = self.firstname +" " + self.lasttname
        # print("The name of the user is:",name)    

        return name

class employee(person):

    def __init__(self,first,last,age,staffNumber):
        super().__init__(first,last,age)
        self.staffNumber= staffNumber


    def __str__(self):
        # a = self.printName() + "," + self.staffNumber
        return super().__str__() + "," + self.staffNumber     

x = person("Yuvraj","Rathod","20")
y = employee("Mayur","Pawar","20","123")

print(x)
# print(y.printName())
print(y)
