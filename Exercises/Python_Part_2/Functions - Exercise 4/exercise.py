def greeter(name,surname):
    print(f'Hello {name} {surname}!')

name_list=['John Doe', 'Tristram Mcbride','Baldwin Preston','Wally Collins']

for name in name_list:
    first_name=name.split(" ")[0]
    last_name=name.split(" ")[1]
    greeter(first_name,last_name)

