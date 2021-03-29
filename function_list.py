# Write your code here :-)
#Functions in list
def func():
    print('Inside func')

def disp():
    print('Inside disp')

def msg():
    print('Inside msg')

lst = [func, disp, msg]
for f in lst:
    f()

############################################
lst1 = [1,2,3,4,5,6]
lst2 = [9,8,7,6,5,4]
maplst = map(lambda n1,n2 : n1+n2,lst1,lst2)
print(list(maplst))
############################################

lst3 = [2,3,8,-4,6,-3]
mapsqr = map(lambda n1:n1*n1,lst3)
print(list(mapsqr))
