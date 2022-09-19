a=int(input())
b=a
c=0
d=1
while a:
    r=a%10
    c+=r
    d*=r
    a=a//10
print(d-c)