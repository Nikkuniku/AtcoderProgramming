n,k=map(int,input().split())
score=[]
for _ in range(n):
    a,b=map(int,input().split())
    score.append(b)
    score.append(a-b)

score=sorted(score,reverse=True)
ans=sum(score[:k])
print(ans)