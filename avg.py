# Write your code here :-)
total_numbers = int(input("How many numbers ? - "))
sum_of_numbers = 0
for x in range(total_numbers):
    sum_of_numbers = sum_of_numbers + float(input(str(x) + " number - "))
print("Avg : " + str(float(sum_of_numbers / total_numbers)))

a, b, c, d, e = 12.34, 234.39, 444.34, 1.23, 34.67
print("{0:8}".format(a))
print("{0:8}".format(b))
print("{0:8}".format(c))
print("{0:8}".format(d))
print("{0:8}".format(e))
