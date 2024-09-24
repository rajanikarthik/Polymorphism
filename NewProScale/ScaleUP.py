import pytest
from datetime import datetime

#Parent class to read age
class Father:
    def __init__(self,age):
        self.FAge=age

#Parent class Mother to read name
class Mother:
    def __init__(self):
        self.MName="Mother Name"

#Polymorphism - deriving child from mother and father class
class Child(Father,Mother):
    def __init__(self, fage,name,age):
        super().__init__(fage)
        Mother.__init__(self)
        self.Name=name
        self.Age=age

    #Function to check Pallindrome
    def palindrome(self):
        self.Name = self.Name.replace(" ", "").lower()

        #Reversing the string and comparing with input string
        if self.Name == self.Name[::-1]: # Success Case
            return "Its Pallindrome: "+ str(int(self.FAge)-int(self.Age))
        else:                            #Failure Case
            return "Its not Pallindrome"

c = Child(50, 'SAM', 9)
if __name__ == "__main__":
    print(c.palindrome())







