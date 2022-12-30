s=list(input())
t=list(input())

n=len(s)
m=len(t)

ans=0
for i in range(n-m+1):
    tmp=0
    for j in range(m):
        p=s[i+j]
        q=t[j]
        if s[i+j]==t[j]:
            tmp+=1
    
    ans=max(ans,tmp)

print(m-ans)