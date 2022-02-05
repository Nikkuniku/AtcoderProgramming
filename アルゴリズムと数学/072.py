A,B=map(int,input().split())

ans=1
for b in range(1,B+1):
    p=B//b
    q=A//b
    if A%b==0:
        q-=1
    
    if p-q>1:
        ans=max(ans,b)

print(ans)