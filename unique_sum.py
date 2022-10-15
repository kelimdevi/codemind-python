n=int(input())
m=list(map(int,input().split()))
b=[]
for i in m:
    if i not in b:
        b.append(i)
        b.sort()
print((sum(b)))