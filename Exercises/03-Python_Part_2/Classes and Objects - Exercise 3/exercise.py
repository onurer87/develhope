
class Animal:
    def __init__(self,legs_count):
        print("Animal object was created")
        self._number_of_legs= legs_count
    
    def runs(self):
        print("Running started")

    def count_legs(self):
        print(f"It has {self._number_of_legs} legs.")

    def return_legs(self):
        return self._number_of_legs
        
animal= Animal(4)
animal.count_legs()
print(animal.return_legs())
print(animal._number_of_legs)