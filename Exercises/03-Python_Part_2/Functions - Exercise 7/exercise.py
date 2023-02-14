def lambdaa(number):
    if number%2==0:
        return number**2
    else:
        pass

my_list= [lambdaa(number) for number in range(5)] 

print(my_list)
