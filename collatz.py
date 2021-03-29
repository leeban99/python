# Write your code here :-)
def collatz(number):
    if int(number) % 2 == 1:
        return 3 * int(number) + 1
    else:
        return int(number) // 2


while 1:
    try:
        _input = input()
        collatz_val = collatz(_input)
        print(collatz_val)
        if collatz_val == 1:
            break
    except ValueError:
        print("String values are not allowed")
