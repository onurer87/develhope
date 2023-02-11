fib_numbers=[]
fib_numbers.append(0)
fib_numbers.append(1)
[fib_numbers.append(fib_numbers[i-2]+fib_numbers[i-1]) for i in range(2,5) ]
print(fib_numbers)