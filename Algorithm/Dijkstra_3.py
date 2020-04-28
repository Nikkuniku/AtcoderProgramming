from collections import deque

class Dijkstra:
    def __init__(self):
        self.matrix=[]

    def add(self,start,end,cost):
        self.matrix.append([start,end,cost])

    def createroot(self,direction):
        #頂点の最大値
        V_max = max([max(i[:2]) for i in self.matrix])

        self.root = [[float('inf')]*(V_max+1) for _ in range(V_max+1)]
        for i in range(V_max+1):
            self.root[i][i] = 0

        #direction ==True の時は無向グラフとする。
        for e in self.matrix:
            self.root[e[0]][e[1]] = e[2]
            if direction==True:
                self.root[e[1]][e[0]] = e[2]

        print(*self.root,sep="\n")

    def shortest_path(self,start,end):
        #頂点の数
        V=len(self.root)

        #距離格納配列
        distance=[float('inf')]*V
        for j in range(V):
            distance[j] = self.root[start][j]

        #確定済み配列
        visited=[0] * V
        visited[start] = 1
        size = 1

        #最短経路を記録する配列
        path =[-1]*V

        while size<V:
            min_distance = float('inf')
            for i in range(V):
                if visited[i]==0 and distance[i] <min_distance:
                    min_distance = distance[i]
                    v = i
            visited[v] = 1
            size+=1
            for x in range(V):
                if distance[x] > distance[v] + self.root[v][x]:
                    distance[x] = distance[v] + self.root[v][x]
                    path[x] = v

        print(distance)
        
        #最短経路の出力
        rooting='{}'.format(end)
        while path[end]!=-1:
            rooting = str(path[end])+'->' +rooting
            end = path[end]

        print(str(start)+'->' + rooting)




i =Dijkstra()


i.add(0,1,1)
i.add(1,2,2)
i.add(1,3,4)
i.add(2,3,2)
i.add(2,4,3)
i.add(3,4,2)
i.add(3,5,1)
i.add(4,6,3)
i.add(5,6,2)

i.createroot(True)
i.shortest_path(0,6)
