n=int(input())
sum=0
s=n*n
while s:
    r=s%10
    sum=sum+r
    s=s//10
if n==sum:
    print("Neon Number")
else:
    print("Not Neon Number")