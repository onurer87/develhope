class Animal:
    def __init__(self,leg_count=4):
        self.num_of_legs=leg_count
        print("Animal object was created")
    def runs(self):
        print('Running started')


dog=Animal()
dog.runs()
