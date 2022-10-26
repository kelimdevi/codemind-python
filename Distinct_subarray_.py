a = int(input())
b = int(input())
c = list(range(a,b+1))
ct = 0
for i in range(0,len(c)+1):
    for j in range(i+1,len(c)+1):
        if int(sum(c[i:j]))%2==1:
            ct+=1
print(ct)