n=int(input())
b=list(map(int,input().split()))
c=[]
ct=0
for i in b:
    if i not in c:
        c.append(i)
for i in c:
    if i%2==0:
        ct+=1
print(ct)