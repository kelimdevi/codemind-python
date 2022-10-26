a = int(input())
b = list(map(int,input().split()))
d = []
for i in b:
    if b.count(i)==1:
        d.append(i)
if len(d)>=1:
    print(*d)
else:
    print("-1")