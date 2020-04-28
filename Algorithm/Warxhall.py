import math

class Warshall:
    def __init__(self):
        self.matrix=[]
        print("Warshell class start! ")

    def add(self,start,end,cost):
        self.matrix.append([start,end,cost])

    def createroots(self):
        N = max([ max(i[:2]) for i in self.matrix])
        self.roots=[[math.inf]*(N+1) for _ in range(N+1)]

        for j in self.matrix:
            self.roots[j[0]][j[1]] = j[2]
            self.roots[j[1]][j[0]] = j[2]

        #自身へのコストは0
        for k in range(N+1):
            self.roots[k][k] = 0

        #グラフ隣接行列
        print(*self.roots,sep="\n")   

    def shortest_path(self,start,end):
        d = self.roots
        L = len(self.roots)

        for k in range(L):
            for i in range(L):
                for j in range(L):
                    d[i][j] = min(d[i][j],d[i][k] + d[k][j])

        print(*d,sep="\n")
        print(d[start][end])


i=Warshall()

# i.add(0,1,2)
# i.add(0,2,3)
# i.add(1,2,1)
# i.add(1,3,2)
# i.add(2,3,4)
# i.add(2,4,2)
# i.add(3,4,3)



i.add(0,1,1)
i.add(0,4,2)
i.add(1,5,3)
i.add(2,6,1) #これを入れると正しい答えが返る
i.add(4,5,2)
i.add(4,3,2)
i.add(5,2,1)
i.add(5,3,2)
i.add(2,3,3)
i.add(3,6,4)

i.createroots()
i.shortest_path(0,6)

