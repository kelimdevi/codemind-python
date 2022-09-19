a=int(input())
for i in range(1,a+1):
    b=int(input())
    f=0
    for j in range(1,b+1):
        if j*j==b:
            f=1
    if f==1:
        print("True")
    else:
        print("False")