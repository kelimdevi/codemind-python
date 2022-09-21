n=int(input())
factorsum=0
for i in range(1,n):
    if n%i==0:
        factorsum+=i
if factorsum>n:
    print("True")
else:
    print("False")