# Write your code here :-)
def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')
indent = 22
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
print(' ' * indent, end='')
