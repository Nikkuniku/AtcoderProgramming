h,w=map(int,input().split())
matrix=[]
for _ in range(h):
    matrix.append(list(map(int,input().split())))
ans=[[0]*h for _ in range(w)]

for i in range(h):
    for j in range(w):
        ans[j][i]=matrix[i][j]

for i in range(w):
    print(*ans[i])