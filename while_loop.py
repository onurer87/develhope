list_names=["Onur","Hasan","Ali","Hakan","Fırat"]
sorted_names=[]

print(hex(list_names[0]))


while len(list_names)>0:
    sorted_names.append(min(list_names))
    list_names.pop(min(list_names))
    print(sorted_names)
else:
    print(f'Sorting is done sorted list is below\n {sorted_names}')