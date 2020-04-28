class Dijkstra:
    def __init__(self):
        self.matrix =[]
        self.start = 1
        self.end = 1
        print("Dijkstr Class is imported!")

    def add(self,ver_from,ver_to,cost):
        self.matrix.append([ver_from,ver_to,cost])

    #始点ノード、終点ノードの設定
    def start_end(self,start_node,end_node):
        self.start = start_node
        self.end =end_node

    def Createadjacencymatrix(self):
        max_ver = max([max(l[:2]) for l in self.matrix])

        #どっち?
        self.adjaMatrix = [[float('inf')]*max_ver for i in range(max_ver)]
        # self.adjaMatrix = [[0]*max_ver for i in range(max_ver)]

        #初期化
        #スタートからスタート自身への距離は0である。
        self.adjaMatrix[self.start-1][self.start-1]=0

        for i in range(len(self.matrix)):
            ver_from = self.matrix[i][0]
            ver_to = self.matrix[i][1]
            edge = self.matrix[i][2]

            self.adjaMatrix[ver_from-1][ver_to-1] = edge   

    def execute(self):
        
        #探索ノード
        searched = []
        #未探索ノード
        unsearched = [i for i in range(self.start+1,self.end+1)]

        #距離のリスト
        distance = [float('inf')]*self.end
        distance[0]=0

        print(searched)
        print(unsearched)

        print(distance)
        k=self.start+1
        while len(unsearched) !=0:
            
            for node_index in unsearched:
                if distance[k] > self.adjaMatrix[k-1][node_index-1]:
                    distance[k] = self.adjaMatrix[k-1][node_index-1]

            min_index = self.adjaMatrix[k-1].index(distance[k])
            unsearched.remove(min_index)
            searched.append(min_index)

            k +=1
            
        print(distance)

i = Dijkstra()

i.add(1,2,2)
i.add(1,3,3)
i.add(2,3,1)
i.add(2,4,2)
i.add(3,4,4)
i.add(3,5,2)
i.add(4,5,3)

i.start_end(1,5)


i.Createadjacencymatrix()
print(*i.adjaMatrix,sep="\n")

i.execute()