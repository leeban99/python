# Write your code here :-)
n = int(input().strip())
if n%2 == 1:
    print("Weird" + str(1))
elif n%2 == 0 & n >=2 & n <= 5:
    print("Not Weird" + str(2))
elif n%2 == 0 & n >=6 & n <= 20:
    print("Weird" + str(3))
elif n%2 == 0 & n>19 & n <= 100:
    print("Not Weird" + str(4))


if n>2 and n<5:
    print("OK")
else:
    print("Not OK")

n = int(input())
for i in range(1,n+1):
    print(i,end='')

q='abc'
print(q.swapcase())
