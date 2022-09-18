n=int(input())
while n:
    a=n//1000
    b=n%1000
    c=b//100
    d=b%100
    e=d//10
    f=d%10
    g=max(a,c,e,f)
    print(g)
    break