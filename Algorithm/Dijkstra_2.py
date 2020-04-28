class Dijkstra():

    def __init__(self):
        self.matrix =[]
        print("Dijkstr Class is imported!")

    def add(self,ver_from,ver_to,cost):
        self.matrix.append([ver_from,ver_to,cost])

    def Createadjacencymatrix(self):
        #終点の最大値Nを取得する
        max_ver = max([max(l[:2]) for l in self.matrix])

        #グラフの終点=N⇒N×Nのゼロ行列を作成する
        self.route= [[float('inf')]*max_ver for i in range(max_ver)]
        # self.adjaMatrix = [[0]*max_ver for i in range(max_ver)]

        # matrixに記録された2つのノードとその間のエッジコストをもとに
        # 隣接行列を作成する
        for i in range(len(self.matrix)):
            ver_from = self.matrix[i][0]
            ver_to = self.matrix[i][1]
            edge = self.matrix[i][2]

            self.route[ver_from-1][ver_to-1] = edge 
            self.route[ver_to-1][ver_from-1]=edge 

    def shortest_path(self,start,end):
        
        self.Createadjacencymatrix()
        N=len(self.route)

        #startからの距離を格納する配列
        distance=[ self.route[int(start)-1][i] for i in range(N) ]
        #探索済みを示す配列
        visit=[0]*N
        #最短経路を示す配列
        path=[start]*N

        # 始点は探索済みとする
        visit[start-1] = 1
        #始点は探索済みとしたためsizeを1にする
        size=1
        
        #初期化
        #始点までの距離は考えないため0にする
        distance[start-1] =0
        #始点までの経路は考えない
        path[start-1] = -1

        while size<N:
            min_distance = float('inf')

            # startから各ノードまでの距離で最短なノードを求める
            for i in range(N):
                if visit[i]==0 and distance[i] < min_distance:
                    min_distance = distance[i]
                    v=i

            #訪れたノードを記録しておく
            visit[v]=1
            # print("visit:{}".format(v))
            #確定したノードの数を1増やす
            size +=1
            
            for x in range(N):
                if self.route[v][x] !=float('inf') and visit[x] ==0:
                    if distance[x] > distance[v] +self.route[v][x]:
                        distance[x] = distance[v] +self.route[v][x]
                        path[x] =v



        print(path)
        print(distance)

        #最短経路出力
        routing ='{}'.format(end)
        a_num = end-1
        while True:
            if path[a_num] !=1:
                routing = str((path[a_num]+1)) +'->' + routing
                a_num = path[a_num]
            else:
                break

        routing = str(1)+'->'+routing

        print(routing)



i = Dijkstra()

i.add(1,2,1)
i.add(1,3,2)
i.add(1,4,5)
i.add(2,3,2)
i.add(2,5,3)
i.add(3,5,2)
i.add(3,6,1)
i.add(4,6,2)
i.add(5,6,4)


i.shortest_path(1,6)

# print(*i.route,sep="\n")