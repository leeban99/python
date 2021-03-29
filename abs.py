# Write your code here :-)
while 1:
    try:
        a = int(input("Enter the no. (0 to exit) - "))
        if a == 0:
            break
        else:
            print(abs(a))
    except ValueError:
        print("Value not type of integer")
        continue

for x in range(5):
    print(x)

