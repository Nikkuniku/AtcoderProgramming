from collections import defaultdict
N = int(input())
d_migishita = defaultdict(int)
d_hidarishita = defaultdict(int)
row = [0]*N
column = [0]*N
for _ in range(N-1):
    r, c = map(int, input().split())
    r -= 1
    c -= 1
    row[r] += 1
    column[c] += 1
    d_migishita[(r-min(r, c), c-min(r, c))] += 1
    d_hidarishita[(r-min(r, N-1-c), c+min(r, N-1-c))] += 1
for i in range(N):
    if row[i] > 0:
        continue
    for j in range(N):
        if column[j] > 0:
            continue
        s = d_migishita[(i-min(i, j), j-min(i, j))]
        t = d_hidarishita[(i-min(i, N-1-j), j+min(i, N-1-j))]
        cnt = row[i]+column[j]+s+t
        if cnt == 0:
            print(i+1, j+1)
            exit()
print(-1)
