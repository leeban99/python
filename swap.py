# Write your code here :-)
#Swap 2 variables without using third variable
a = int(input("Input variable a : "))
b = int(input("Input variable b : "))
print('a = {}'.format(a))
print('b = {}'.format(b))
a = a + b
b = a - b
a = a - b
print('b = {}'.format(b))
print('a = {}'.format(a))
