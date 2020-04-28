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

    def Shortest_path(self,start,end):
        #頂点の数
        V=len(self.root)
        distance=[float('inf')]*V
        #スタート自身の距離は0に初期化
        distance[start] = 0

        #探索済みか判定する配列
        visit = [0]*V
        #初期値は探索済みとする
        visit[start]=1
        size =1
        unserach =0

        ready = start
        while size<V:
            for v in range(V):
                if visit[v] == 0 and self.root[ready][v]!=float('inf'):
                    unserach =v
                    size +=1
                    break
            
            for x in range(V):
                if distance[x]!=float('inf') and self.root[x][unserach] != float('inf')and visit[x] == 1:
                    distance[unserach] = min (distance[unserach] , distance[x]+self.root[x][unserach])
                    visit[unserach] = 1
                    ready = unserach
                    

        print(distance)



i = BFS()

i.add(0,1,1)
i.add(1,2,1)
i.add(1,3,1)
i.add(2,3,1)
i.add(3,4,1)

i.CreateRoot()


i.Shortest_path(2,1)


