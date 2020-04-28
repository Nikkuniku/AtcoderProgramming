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
        queue=[start]


        while size<V:
            for v in range(V):
                if self.root[queue[0]][v]!=float('inf') and visited[v]==0:
                    queue.append(v)

            for d in queue:
                if distance[d] > distance[queue[0]] + self.root[queue[0]][d]:
                    distance[d] = distance[queue[0]] + self.root[queue[0]][d]
                    visited[d] =1
                    size+=1

            del queue[0]
        

        print(distance)







i = BFS()

i.add(0,1,1)
i.add(1,2,1)
i.add(1,3,1)
i.add(2,3,1)
i.add(3,4,1)

i.CreateRoot()
for j in range(5):
    i.shortest_path(j,1)
