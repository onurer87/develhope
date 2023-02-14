list1 = ["lion", "monkey", "dog","fish"]
tuple1 = ("lion", "monkey", "dog","fish")
set1 = {"lion", "monkey", "dog","fish"}
dict1 = {"lion":"land", "monkey":"land", "dog":"land","fish":"water"}

for i in range(0,4):
    print(f'list1 value {list1[i]},\ntuple1 value {tuple1[i]}')


for y in set1:
    print(f'set1 value {y}')

for x in dict1:
    if dict1[x]=="land":
        print(f'{x} live in {dict1[x]}')


