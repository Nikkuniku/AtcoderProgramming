n=int(input())

d={}

for _ in range(n):
    a=int(input())
    if a not in d:
        d[a]=1
    else:
        if d[a]==1:
            d[a]=0
        else:
            d[a]=1

ans=0
for _,v in d.items():
    if v==1:
        ans+=1

print(ans)