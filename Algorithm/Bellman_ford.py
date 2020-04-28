class Bellman_ford():
    def __init__(self):
        self.matrix=[]
        print("Bellman-ford class is imported!")

    
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

        print(*self.root,sep="\n")

    def shortest_path(self,start,end):
        #V:頂点の個数
        #E:辺の個数
        V =  max([ max(i[:2]) for i in self.matrix])
        # E = len(self.matrix)

        #距離配列
        d = [float('inf')]*(V+1)
        #始点なので0で初期化
        d[start]=0
        isNegCycle = False

        for i in range(V):
            isupdate = False
            for e in self.matrix:
                if d[e[1]] > d[e[0]] + e[2]:
                    d[e[1]] =  d[e[0]] + e[2]
                    isupdate = True
                    #iは0から始まるので、i==V-iは更新をV回行ったことになる。
                    if i == V-1:
                        isNegCycle =True
                        break
            
            if isupdate ==False:
                break

        if isNegCycle == True:
            print("Negative cycle exist")
        else:
            # print(*d,sep="\n")
            print(d[end])

i = Bellman_ford()

i.add(0,1,2)
i.add(0,3,4)
i.add(1,2,3)
i.add(2,3,-2)
i.add(2,5,2)
i.add(3,4,2)
i.add(3,5,4)
i.add(4,5,1)

# i.CreateRoot()
i.shortest_path(2,3)
