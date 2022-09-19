a=int(input())
for i in range(a):
    b,c=map(int,input().split())
    cnt=0
    for i in range(b,c+1):
        if i%10==2 or i%10==3 or i%10==9:
            cnt+=1
    print(cnt)