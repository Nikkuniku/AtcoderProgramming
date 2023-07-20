a,b=map(int,input().split())
ans=0
for i in range(1,a+1):
    lim = b+1 if i==a else 30
    for j in range(1,lim):
        if i==j:
            ans+=1
print(ans)
    