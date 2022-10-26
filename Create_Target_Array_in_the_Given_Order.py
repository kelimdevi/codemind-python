a = int(input())
b = list(map(int,input().split()))
c = int(input())
d = list(map(int,input().split()))
e = []
j = 0
for i in range(0,len(b)):
    e.insert(d[i],b[j])
    j+=1
print(*e)