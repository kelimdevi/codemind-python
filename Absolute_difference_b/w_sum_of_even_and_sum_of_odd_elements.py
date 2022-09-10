n=int(input())
a=list(map(int,input().split()))
c=[]
d=[]
for i in a:
    if i%2==0:
        c.append(i)
    if i%2==1:
        d.append(i)
print(abs(sum(c)-sum(d)))