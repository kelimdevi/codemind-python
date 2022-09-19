n=int(input())
reverse=0
f=0
while n:
    a=n%10
    reverse=(reverse*10)+a
    n=n//10
    if n==reverse:
        f=1
        break
if f==1:
    print("True")
else:
    print("False")