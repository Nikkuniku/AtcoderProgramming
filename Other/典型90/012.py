class UnionFind:
    def __init__(self, n):
        # 負  : 根であることを示す。絶対値はランクを示す
        # 非負: 根でないことを示す。値は親を示す
        self.table = [-1] * n
 
    def root(self, x):
        stack = []
        tbl = self.table
        while tbl[x] >= 0:
            stack.append(x)
            x = tbl[x]
        for y in stack:
            tbl[y] = x
        return x
 
    def find(self, x, y):
        return self.root(x) == self.root(y)
 
    def unite(self, x, y):
        r1 = self.root(x)
        r2 = self.root(y)
        if r1 == r2:
            return
        # ランクの取得
        d1 = self.table[r1]
        d2 = self.table[r2]
        if d1 <= d2:
            self.table[r2] = r1
            if d1 == d2:
                self.table[r1] -= 1
        else:
            self.table[r1] = r2

h,w=map(int,input().split())
q=int(input())
isred=[False]*(h*w)
ins = UnionFind(h*w)
answers=[]


def cell(r,c):
    return (r-1)*w + c-1

for _ in range(q):
    query=list(map(int,input().split()))

    q_i=query[0]
    if q_i==1:
        r_i,c_i = query[1],query[2]
        isred[cell(r_i,c_i)]=True

        # up
        if 0<=cell(r_i-1,c_i)<h*w:
            if isred[cell(r_i-1,c_i)]==True:
                ins.unite(cell(r_i-1,c_i),cell(r_i,c_i))
        #down
        if 0<=cell(r_i+1,c_i)<h*w:
            if isred[cell(r_i+1,c_i)]==True:
                ins.unite(cell(r_i+1,c_i),cell(r_i,c_i))
        #left
        if 0<=cell(r_i,c_i-1)<h*w and cell(r_i,c_i)%w>0:
            if isred[cell(r_i,c_i-1)]==True:
                ins.unite(cell(r_i,c_i-1),cell(r_i,c_i))
        #right
        if 0<=cell(r_i,c_i+1)<h*w and cell(r_i,c_i)%w<w-1:
            if isred[cell(r_i,c_i+1)]==True:
                ins.unite(cell(r_i,c_i+1),cell(r_i,c_i))

    else:
        ans='No'
        r_1,c_1 = query[1],query[2]
        r_2,c_2 = query[3],query[4]
        if cell(r_1,c_1)==cell(r_2,c_2):
            if isred[cell(r_1,c_1)]:
                ans='Yes'
        else:
            if ins.find(cell(r_1,c_1),cell(r_2,c_2)):
                ans='Yes'

        answers.append(ans)

print(*answers,sep="\n")