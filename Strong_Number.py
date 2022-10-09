import math
a=int(input())
sum=0
for i in str(a):
    sum+=math.factorial(int(i))
if sum==a:
    print("The number",a,"is a strong number")
else:
    print("The number",a,"is not a strong number")