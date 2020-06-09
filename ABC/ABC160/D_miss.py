import sys
# input処理を高速化する
input = sys.stdin.readline

N,X,Y = map(int,input().split())

from collections import deque

class BFS():
    def __init__(self):
        self.matrix=[]
        print("BFS class is imported!")

    def add(self,start,end,cost):
        self.matrix.append([start,end,cost])
    
    def CreateRoot(self):
        #頂点の数
        V = max([ max(i[:2]) for i in self.matrix])


        #隣接行列の作成
        self.root = [[float('inf')]*(V+1) for _ in range(V+1)]

        #その点自身の距離は0に初期化
        for j in range(V+1):
            self.root[j][j] = 0

        for e in self.matrix:
            self.root[e[0]][e[1]] = e[2]
            self.root[e[1]][e[0]] = e[2]

        # print(*self.root,sep="\n")

    def shortest_path(self,start,end):
        #頂点の数
        V = len(self.root)

        #startから各点までの距離を格納
        distance=[float('inf')] * V
        distance[start] =0

        #visited:探索済みの点
        #size:探索済みの頂点数
        visited=[0]*V
        visited[start] = 1
        size = 1

        #キュー
        d =deque()
        d.append(start)

        while size<V:
            for v in range(V):
                if self.root[d[0]][v]!=float('inf') and visited[v]==0:
                    d.append(v)

            for w in d:
                if distance[w] > distance[d[0]] + self.root[d[0]][w]:
                    distance[w] = distance[d[0]] + self.root[d[0]][w]
                    visited[w] =1
                    size+=1

            d.popleft()       

        return distance

i=BFS()

for j in range(N-1):
    i.add(j,j+1,1)

i.add(X-1,Y-1,1)

i.CreateRoot()

matrix=[]
for j in range(N):
    matrix.append(i.shortest_path(j,j+1))


print(*matrix,sep="\n")

Distances=[0]*(N+1)

for i in range(N):
    for j in range(i+1,N):
        Distances[matrix[i][j]]+=1 

for k in range(1,N):
    print(Distances[k])
