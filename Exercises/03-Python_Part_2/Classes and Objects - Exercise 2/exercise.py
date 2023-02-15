
class Animal:
    def __init__(self,leg_count=4):
        self.num_of_legs=leg_count
        print("Animal object was created")
    def runs(self):
        print('Running started')
    def count_legs(self):
        print(f'Number of legs,{self.num_of_legs}')
    def return_legs(self):
        return self.num_of_legs


dog=Animal()
dog.runs()
dog.count_legs()
print(dog.return_legs())
print(dog.num_of_legs)

