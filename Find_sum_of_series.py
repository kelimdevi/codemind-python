a=int(input())
b=0
for i in range(1,a+1):
    b+=1/i
res="{:.2f}".format(b)
print(res)