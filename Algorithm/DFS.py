from collections import deque

class DFS():
    def __init__(self):
        self.matrix=[]
        print("DFS class is imported!")

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
        stack =deque()
        stack.append(start)

        while size<V:
            indexs=len(stack)-1
            for v in range(V):
                if self.root[stack[indexs]][v]!=float('inf') and visited[v]==0:
                    stack.append(v)

            l_index = len(stack)-1

            for w in stack:
                if distance[w] > distance[stack[l_index]] + self.root[stack[l_index]][w]:
                    distance[w] = distance[stack[l_index]] + self.root[stack[l_index]][w]
                    visited[w] =1
                    size+=1
            stack.pop()       

        print(distance)







i = DFS()

i.add(0,1,1)
i.add(1,2,1)
i.add(1,3,1)
i.add(2,3,1)
i.add(3,4,1)

i.CreateRoot()

i.shortest_path(1,1)
