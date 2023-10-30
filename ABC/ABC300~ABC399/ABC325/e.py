N,A,B,C=map(int,input().split())
Edge=[[] for _ in range(2*N)]
D=[]
for _ in range(N):
    D.append(list(map(int,input().split())))

from heapq import heappush, heappop
INF=1<<60
dist = [INF] *(2*N)
hq = [(0, 0)] # (distance, node)
dist[0] = 0
seen = [False] * (2*N)
while hq:
    v = heappop(hq)[1] # node
    seen[v] = True
    if v<N:
        for to in range(N):
            # 社用車の世界
            if seen[to]==False and dist[v]+A*D[v][to]<dist[to]:
                dist[to] = dist[v] + A*D[v][to]
                heappush(hq, (dist[to], to))                
            # 社用車→電車の世界
            if seen[to+N]==False and dist[v]+A*D[v][to]<dist[to+N]:
                dist[to+N] = dist[v] + A*D[v][to]
                heappush(hq, (dist[to+N], to+N))
    else:
        w=v%N
        for to in range(N):
            if seen[to+N] == False and dist[v] + B*D[v%N][to] +C< dist[to+N]:
                dist[to+N] =  dist[v] + B*D[v%N][to] +C
                heappush(hq, (dist[to+N], to+N))
print(dist[-1])