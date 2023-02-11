from random import randint

def random_list_summer():
    number_list=[]
    sum=0
    for i in range(0,14):
        number_list.append(randint(-100,100))
    print(number_list)
    
    for number in number_list:
        sum+=number
    print(sum)


random_list_summer()