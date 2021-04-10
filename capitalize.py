# Write your code here :-)
size, price = map(int, input().split())
print(size)
print(price)
sss=[1,3,2,5,8]
sss.sort()
print(sss[len(sss)-2])

ss='abcd'
for i in range(len(ss)):
    print(ss[i:i+2])

s='testing python'
s1=s.split()

print(s.capitalize())
print(s1)


s = input()
for x in s[:].split():
    s = s.replace(x, x.capitalize())
    print(x)
    print(s[:])
print(s)

a = [1,2,3,4,5,5]
print(a.count(5))
print(a.count(2))
