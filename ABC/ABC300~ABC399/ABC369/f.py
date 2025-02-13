from sortedcontainers import SortedList
from collections import defaultdict

H, W, N = map(int, input().split())
Rows = SortedList()
Cols = defaultdict(list)
Coins = [list(map(int, input().split())) for _ in range(N)]
zip_Row=set()
zip_Col=set()
for i in range(N):
    r,c=Coins[i]   
    zip_Row.add(r)
    zip_Col.add(c)
# 座圧
map_row=defaultdict(int)
map_col=defaultdict(int)
for i,v in enumerate(sorted(zip_Row)):
    map_row[v]=i
for i,v in enumerate(sorted(zip_Col)):
    map_col[v]=i
zip_Coins=[]
for r,c in Coins:
    zip_Coins.append((map_row[r],map_col[c]))
Coins.sort(key=lambda x: x[1])
Coins.sort(key=lambda x: x[0])
dp = [0] * (N + 1)
Cols[1].append(1)
Rows.add(1)
prev=[-1]*(N+1)
for i in range(N):
    r, c = Coins[i]
    idx=Rows.bisect_right(r-1)
    if 0<idx:


    Rows.add(r)
    Cols[r].append(c)
    