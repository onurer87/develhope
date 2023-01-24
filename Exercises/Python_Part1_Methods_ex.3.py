num1 = 1122334455666

#cast num1 to string and assign to num1_str
num1_str=str(num1)
#check the length of the string
print(len(num1_str))
#get the third element of string (the one in the 3rd order)
print(num1_str[2])
#get the 3-5 elements of string (both inclusive) by string slicing
print(num1_str[2:5:1])
#check if num2 in string (cast if necessary)
num2= 2233
print(str(num2) in num1_str)
#check if num3 in string (cast if necessary)
num3=23232
print(str(num3) in num1_str)
#concatenate 0 to the string from left and assign to string_with_0
string_with_0= '0'+num1_str
print(string_with_0)
#get the characters of string_with_0 from start to position 4 (end point exclusive)
print(string_with_0[:4])
#get the characters of string_with_0 from position 5 until the end
print(string_with_0[4:])
#use negative indexing to reach the "567" string_with_0
#number '7' is added to the string to solve this problem
string_with_0=string_with_0+'7'
print(string_with_0[-5]+string_with_0[-4]+string_with_0[-1])







