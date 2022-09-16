n=int(input())
a=list(map(int,input().split()))
lasteven=0
for i in range(n):
    if a[i]%2==0:
        lasteven=i
print(lasteven)