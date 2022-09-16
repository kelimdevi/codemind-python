n=int(input())
a=list(map(int,input().split()))
lastodd=0
for i in range(n):
    if a[i]%2==1:
        lastodd=i
print(lastodd)
        