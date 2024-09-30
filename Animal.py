# Just some testing
class Animal:
    # class variable
    zoo_name = "San Francisco Zoo"

    def __init__(self, type: str, name: str):
        self.type = type
        self.name = name
    
    def change_name(self, new_name):
        self.name = new_name
    
    def __str__(self):
        return f"{self.name} the {self.type} is in the {Animal.zoo_name}."

obj1 = Animal("Tiger", "Teddy")
print(obj1)