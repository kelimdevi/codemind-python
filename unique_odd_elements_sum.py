n=int(input())
a=list(map(int,input().split()))
b=[]
sum=0
for i in a:
    if i not in b:
        b.append(i)
for i in b:
    if i%2==1:
        sum+=i
print(sum)
        