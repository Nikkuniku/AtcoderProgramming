import sys
sys.setrecursionlimit(100000000)
from collections import deque
import collections
n, m = map(int, input().split())
edge = [[] for _ in range(n)]
A=[]
B=[]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)
    A.append(a)
    B.append(b)

color = [0]*n
def dfs(v,pcolor):
    for e in edge[v]:
        if color[e]==0:
            color[e]=-pcolor
            dfs(e,-pcolor)
            
for i in range(n):
    if color[i]==0:
        color[i]=1
        dfs(i,1)

ans='Yes'
for j in range(m):
    if color[A[j]]==color[B[j]]:
        ans='No'
        break

print(ans)