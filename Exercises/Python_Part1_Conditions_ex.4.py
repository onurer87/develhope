import random

number1 = random.randint(-100,100)
number2 = random.randint(-100,100)

if abs(number1) > abs(number2):
    print("number1's absolute value is greater than number2's absolute value")
elif abs(number2) > abs(number1):
    print("number2's absolute value is greater than number1's absolute value")
else:
    print("number1's absolute value is equal to number2's absolute value")