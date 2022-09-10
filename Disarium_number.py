n=int(input())
nd=n
a=0
b=0
cnt=0
sum=0
while n:
    a=a*10+n%10
    n=n//10
    cnt+=1
while a:
    for i in range(1,cnt+1):
        b=(a%10)**i
        a=a//10
        i+=1
        sum+=b
if sum==nd:
    print("True")
else:
    print("False")