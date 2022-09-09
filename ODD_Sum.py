a=int(input())
b=list(map(int,input().split()))
sum=0
for i in range(len(b)):
    if b[i]%2==1:
        sum+=b[i]
print(sum)