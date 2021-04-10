# Write your code here :-)
name,score = ['Shadab','Varun','Sarvesh','Harsh'],[8,8.9,9.5,10]
V,D=set(),{}
for _ in range(4):
    V.add(score[_])
    D[name[_]]=score[_]
V.discard(min(V))
M=min(V)
V.clear()
L=list(V)
for key, value in D.items():
    if M == value:
        L.append(key)
L.sort()
if len(L) != 1:
    print("\n".join(L))
else:
    print(L[0])

a = [[raw_input(), float(raw_input())] for i in xrange(int(raw_input()))]
