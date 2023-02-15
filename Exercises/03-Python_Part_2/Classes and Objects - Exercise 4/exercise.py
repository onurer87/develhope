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
        
class Dog(Animal):
    def __init__(self, legs_count, name_of_dog):
        super().__init__(legs_count)
        self._name_of_dog=name_of_dog
        print(self._name_of_dog)
        print('woof woof')
        self.count_legs()

dog=Dog(4,"John")