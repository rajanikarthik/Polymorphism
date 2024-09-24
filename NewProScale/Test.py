class BaseClass:
    def __init__(self):
        self.base_var = "Base class variable"

class DerivedClass(BaseClass):
    def __init__(self):
        super().__init__()  # Initialize BaseClass
        self.child_var = "Child class variable"

    def show_variables(self):
        # Access base class variable
        print(f"Base class variable: {self.base_var}")
        # Access child class variable
        print(f"Child class variable: {self.child_var}")

# Create object of DerivedClass
obj = DerivedClass()
obj.show_variables()