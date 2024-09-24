from datetime import datetime
class Father:
    def __init__(self,age):
        self.FAge=age

class Mother:
    MName="myname"
    def __init__(self,name):
        self.MName=name

class Child(Father,Mother):
    def __init__(self, fage,name,age):
        super().__init__(fage)
        self.Name=name
        self.Age=age
    def pallindrome(self):
        self.Name = self.Name.replace(" ", "").lower()
        if self.Name == self.Name[::-1]:
            return "Its Pallindrome: "+ str(int(self.FAge)-int(self.Age))
        else:
            return "It's not Pallindrome"


FAge = input("Enter Father's Age: ")
CName = input("Enter Child's Name: ")
CAge = input("Enter Child's Age: ")

#b=Mother('NewName')
c=Child(FAge,CName,CAge)
print(c.pallindrome())




