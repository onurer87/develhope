import random

number1 = random.randint(1,100)
number2 = random.randint(1,100)

# Compare the numbers to eachother 

if number1>number2:
    print("number1 is greater than number2")
elif number2>number1:
    print('number2 is greater than number1')
else:
    print('number2 is equal to number1')
