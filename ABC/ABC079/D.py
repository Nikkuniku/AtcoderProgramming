H,W=map(int,input().split())
grid=[]
for _ in range(10):
    grid.append(list(map(int,input().split())))

Wall=[]
for _ in range(H):
    Wall.append(list(map(int,input().split())))


d=[0]*10
for start in range(10):

    #距離格納配列
    distance=grid[start]

    #確定済み配列
    visited=[0] * 10
    visited[start] = 1
    size = 1

    while size<10:
        min_distance = 10**9
        for i in range(10):
            if visited[i]==0 and distance[i] <min_distance:
                min_distance = distance[i]
                v = i

        visited[v] = 1
        size+=1

        for x in range(10):
            if distance[x] > distance[v] + grid[v][x]:
                distance[x] = distance[v] + grid[v][x]

    d[start]=distance[1]

ans=0
for i in range(H):
    for j in range(W):
        if Wall[i][j]==-1:
            continue
        else:
            ans+=d[Wall[i][j]]

print(ans)
