N = int(input())
X = [sorted(list(map(int, input().split()))) for _ in range(4)]
Y = []
for i in range(4):
    for j in range(N):
        Y.append((X[i][j], i))
Y.sort()
ans=1<<60
from bisect import bisect_left
for i in range(4*N):
    y,j=Y[i]
    tmp=[]
    for k in range(4):
        if k==j:
            continue
        idx=bisect_left(X[k],y)
        if idx==N:
            continue
        tmp.append(X[k][idx])
    if len(tmp)==3:
        ans=min(ans,max(tmp)-y)
print(ans)
    