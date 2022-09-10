n=int(input())
b=list(map(int,input().split()))
lasteven=0
for i in range(n):
    if b[i]%2==0:
        lasteven=i
print(lasteven)
