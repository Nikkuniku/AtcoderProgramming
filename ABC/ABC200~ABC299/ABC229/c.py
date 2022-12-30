n,w=map(int,input().split())
cheese=[]

for _ in range(n):
    a,b=map(int,input().split())
    cheese.append([a,b])

cheese =sorted(cheese,key=lambda x:x[0],reverse=True)

ans=0
cnt=0
for i in range(n):
    if cnt+cheese[i][1]>w:
        eat=w-cnt
        ans+=cheese[i][0]*eat
        break
    else:
        eat=cheese[i][1]
        cnt+=eat
        ans+=cheese[i][0]*eat

print(ans)