s=input()
n=len(s)

d={}
v=s[-1]
d[v]=1
ans=0
for i in range(n-2,-1,-1):
    p=s[i]
    if p in d:
        d[p]+=1
    else:
        d[p]=1

    if p==v:
        for a,b in d.items():
            if a==p:
                continue
            else:
                ans+=b
                d[p]+=b
                d[a]=0
    
    v=p

print(ans)