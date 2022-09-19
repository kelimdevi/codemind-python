a=int(input())
for i in range(a):
    a=int(input())
    b=str(a)
    c=int(b[::-1])
    if a==c:
        print("True")
    else:
        print("False")