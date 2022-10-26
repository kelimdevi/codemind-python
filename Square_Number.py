a=int(input())
flag=0
for i in range(1,a+1):
    if i*i==a:
        flag=1
if flag==1:
    print("True")
else:
    print("False")