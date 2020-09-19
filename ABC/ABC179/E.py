n,x,m=map(int,input().split())

total = x

a=x
for i in range(n):
    r = a%m
    if a==0:
        break
    else:
        a=(r**2)%m
        total+=a

print(total)
        

