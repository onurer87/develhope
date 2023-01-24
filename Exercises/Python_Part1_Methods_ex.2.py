#convert num1 to float and assign to itself
#convert num2 to int and assign to itself
#convert num3 to complex and assign to itself
#use round method for num4 and assign to itself
#use round method for num5 and assign to itself
#print them all
#print their types
# 

num1 = 1.3
num2 = 2.3
num3 = 1j 
num4 = 1.4 
num5 = 1.5

num1=float(num1)
num2=int(num2)
num3=complex(num3)
num4=round(num4)
num5=round(num5)
list=[num1,num2,num3,num4,num5]
for i in list:

    print(i, type(i))