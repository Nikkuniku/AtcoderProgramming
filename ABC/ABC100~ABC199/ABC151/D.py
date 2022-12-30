H,W=map(int,input().split())
maze=[]
maze.append(['#']*(W+2))
for _ in range(H):
    maze.append(['#']+list(input())+['#'])
maze.append(['#']*(W+2))
ans=0

# print(*maze,sep="\n")

from collections import deque

for h in range(1,H+1):
    for w in range(1,W+1):
        if maze[h][w]=='#':
            continue

        dist=[[-1]*(W+2) for _ in range(H+2)]

        d=deque([[h,w]])
        dist[h][w]=0
        while d:
            v=d.popleft()
            i=v[0]
            j=v[1]
            # 左上
            if i==1 and j==1:
                if dist[i+1][j]==-1:
                    if maze[i+1][j]=='.':
                        dist[i+1][j]=dist[i][j]+1
                        d.append([i+1,j])
                if dist[i][j+1]==-1:
                    if maze[i][j+1]=='.':
                        dist[i][j+1]=dist[i][j]+1
                        d.append([i,j+1])
            # 右上
            elif i==1 and j==W:
                if dist[i+1][j]==-1:
                    if maze[i+1][j]=='.' :
                        dist[i+1][j]=dist[i][j]+1
                        d.append([i+1,j])
                if dist[i][j-1]==-1:    
                    if maze[i][j-1]=='.':
                        dist[i][j-1]=dist[i][j]+1
                        d.append([i,j-1])  
            # 上端
            elif i==1:
                if dist[i+1][j]==-1:
                    if maze[i+1][j]=='.':
                        dist[i+1][j]=dist[i][j]+1
                        d.append([i+1,j])
                if dist[i][j+1]==-1:
                    if maze[i][j+1]=='.':
                        dist[i][j+1]=dist[i][j]+1
                        d.append([i,j+1])
                if dist[i][j-1]==-1:    
                    if maze[i][j-1]=='.':
                        dist[i][j-1]=dist[i][j]+1
                        d.append([i,j-1])  
            # 左下
            elif i==H and j==1:
                if dist[i-1][j]==-1:
                    if maze[i-1][j]=='.':
                        dist[i-1][j]=dist[i][j]+1
                        d.append([i-1,j])
                if dist[i][j+1]==-1:
                    if maze[i][j+1]=='.':
                        dist[i][j+1]=dist[i][j]+1
                        d.append([i,j+1]) 
            # 右下
            elif i==H and j==W:
                if dist[i-1][j]==-1:
                    if maze[i-1][j]=='.' :
                        dist[i-1][j]=dist[i][j]+1
                        d.append([i-1,j])
                if dist[i][j-1]==-1:    
                    if maze[i][j-1]=='.':
                        dist[i][j-1]=dist[i][j]+1
                        d.append([i,j-1])     
            # 下端
            elif i==H:
                if dist[i-1][j]==-1:
                    if maze[i-1][j]=='.' :
                        dist[i-1][j]=dist[i][j]+1
                        d.append([i-1,j])
                if dist[i][j-1]==-1:    
                    if maze[i][j-1]=='.':
                        dist[i][j-1]=dist[i][j]+1
                        d.append([i,j-1])    
                if dist[i][j+1]==-1:
                    if maze[i][j+1]=='.':
                        dist[i][j+1]=dist[i][j]+1
                        d.append([i,j+1])
            # 左端   
            elif j==1:
                if dist[i-1][j]==-1:
                    if maze[i-1][j]=='.' :
                        dist[i-1][j]=dist[i][j]+1
                        d.append([i-1,j])
                if dist[i+1][j]==-1:    
                    if maze[i+1][j]=='.':
                        dist[i+1][j]=dist[i][j]+1
                        d.append([i+1,j])    
                if dist[i][j+1]==-1:
                    if maze[i][j+1]=='.':
                        dist[i][j+1]=dist[i][j]+1
                        d.append([i,j+1])   
            # 右端  
            elif j==W:
                if dist[i-1][j]==-1:
                    if maze[i-1][j]=='.' :
                        dist[i-1][j]=dist[i][j]+1
                        d.append([i-1,j])
                if dist[i+1][j]==-1:    
                    if maze[i+1][j]=='.':
                        dist[i+1][j]=dist[i][j]+1
                        d.append([i+1,j])    
                if dist[i][j-1]==-1:
                    if maze[i][j-1]=='.':
                        dist[i][j-1]=dist[i][j]+1
                        d.append([i,j-1])
            else:
                if dist[i-1][j]==-1:
                    if maze[i-1][j]=='.' :
                        dist[i-1][j]=dist[i][j]+1
                        d.append([i-1,j])
                if dist[i+1][j]==-1:    
                    if maze[i+1][j]=='.':
                        dist[i+1][j]=dist[i][j]+1
                        d.append([i+1,j])    
                if dist[i][j-1]==-1:
                    if maze[i][j-1]=='.':
                        dist[i][j-1]=dist[i][j]+1
                        d.append([i,j-1])
                if dist[i][j+1]==-1:
                    if maze[i][j+1]=='.':
                        dist[i][j+1]=dist[i][j]+1
                        d.append([i,j+1])   

        ans=max(ans,max(list(map(lambda x: max(x), dist))))

print(ans)