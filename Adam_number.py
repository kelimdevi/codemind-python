n=int(input())
a=n*n
b=0
c=0
d=0
while n:
    r=n%10
    b=b*10+r
    n=n//10
a2=b*b
while a2:
    r=a2%10
    c=c*10+r
    a2=a2//10
if a==c:
    print("True")
else:
    print("False")