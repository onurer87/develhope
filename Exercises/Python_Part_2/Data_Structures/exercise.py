list1 = ["lion", "monkey", "dog","fish"]
tuple1 = ("lion", "monkey", "dog","fish")
set1 = {"lion", "monkey", "dog","fish"}
dict1 = {"lion":4, "monkey":2, "dog":4,"fish":2}

#1
print(f'Length of list1 is {len(list1)},')
print(f'Length of tuple1 is {len(tuple1)},')
print(f'Length of set1 is {len(set1)},')
print(f'Length of dict1 is {len(dict1)}.')

#2
print(f'First element of list1 is {list1[0]},\nFirst element of tuple1 is {tuple1[0]}.')

#3
print(dict1["lion"])

#4
list1[1]="rabbit"
print(list1)
#5
tuple1[1]="rabbit" #tuples are immutable so you cannot assign new items/values

#6
list1.append('monkey')

#7
list1.remove("rabbit")

#8
dict1["fish"]=0
