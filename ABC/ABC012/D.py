N,M=map(int,input().split())

# 距離初期化
inf=float('inf')
dist=[[inf]*N for _ in range(N)]
for i in range(N):
    dist[i][i]=0

for _ in range(M):
    a,b,t=map(int,input().split())
    a,b=a-1,b-1

    dist[a][b]=t
    dist[b][a]=t


for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j]=min(dist[i][j],dist[i][k] + dist[k][j] )


ans=inf

for e in dist:
    ans=min(ans,max(e))
print(ans)