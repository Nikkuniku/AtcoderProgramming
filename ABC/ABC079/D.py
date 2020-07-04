H,W=map(int,input().split())
grid=[]
for _ in range(10):
    grid.append(list(map(int,input().split())))

Wall=[]
for _ in range(2):
    Wall.append(list(map(int,input().split())))


Cost=[grid[Num][0] for Num in range(1,10)]
for a in range(1,9):
    visited=[0]*10
    visited[a]=1
    for b in range(1,9):
        if visited[b]==1:
            continue
        Cost[a]=min(Cost[a],grid[a][b]+grid[b][0])
        visited[b]=1
        for c in range(1,9):
            if visited[c]==1:
                continue
            Cost[a]=min(Cost[a],grid[a][b]+grid[b][c]+grid[c][0])
            visited[c]=1
            for d in range(1,9):
                if visited[d]==1:
                    continue
                Cost[a]=min(Cost[a],grid[a][b]+grid[b][c]+grid[c][d]+grid[d][0])
                visited[d]=1
                for e in range(1,9):
                    if visited[e]==1:
                        continue
                    Cost[a]=min(Cost[a],grid[a][b]+grid[b][c]+grid[c][d]+grid[d][e]+grid[e][0])
                    visited[e]=1
                    for f in range(1,9):
                        if visited[f]==1:
                            continue
                        Cost[a]=min(Cost[a],grid[a][b]+grid[b][c]+grid[c][d]+grid[d][e]+grid[e][f]+grid[f][0])
                        visited[f]=1
                        for g in range(1,9):
                            if visited[g]==1:
                                continue
                            Cost[a]=min(Cost[a],grid[a][b]+grid[b][c]+grid[c][d]+grid[d][e]+grid[e][f]+grid[f][g]+grid[g][0])
                            visited[g]=1
                            for h in range(1,9):
                                if visited[h]==1:
                                    continue
                                Cost[a]=min(Cost[a],grid[a][b]+grid[b][c]+grid[c][d]+grid[d][e]+grid[e][f]+grid[f][g]+grid[g][h]+grid[h][0])

print(Cost)
