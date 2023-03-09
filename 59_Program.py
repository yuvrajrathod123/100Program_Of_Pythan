
# single inheritance

class user:
    def __init__(self,name):
        self.name = name

    def display_name(self):
        print("Name:", self.name)    

class programmer(user):
     def __init__(self,name):
        self.name = name

     def display_data(self):
        print("leraning python is interesting")


obj1 = programmer("yuvraj")
obj1.display_data()
obj1.display_name()

# obj2 = user()