n=int(input())
b=list(map(int,input().split()))
lastodd=0
for i in range(n):
    if b[i]%2==1:
        lastodd=i
print(lastodd)
