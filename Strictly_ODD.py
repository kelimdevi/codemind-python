n=int(input())
m=list(map(int,input().split()))
o=[]
p=[]
for i in range(len(m)):
    if i%2==1 and m[i]%2==1:
        o.append(i)
for j in m:
    if j%2==1:
        p.append(i)
if len(o)==len(p):
    print("True")
else:
    print("False")