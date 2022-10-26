a,b = map(int,input().split())
c = list(map(int,input().split()))
ct = 0
for i in range(0,len(c)+1):
    for j in range(i+1,len(c)+1):
        if sum(c[i:j])==b:
            ct+=1
print(ct)