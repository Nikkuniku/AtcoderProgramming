N = int(input())
ans = [['.']*N for _ in range(N)]

dxy0 = [(0, 0), (0, 1), (1, 0)]
dxy1 = [(0, 0), (0, 1), (1, 1)]
dxy2 = [(0, 0), (1, 0), (1, 1)]
dxy3 = [(0, 1), (1, 0), (1, 1)]
# 最初
for i, j in [(0, 0)]:
    for dx, dy in dxy0:
        ni = i+dx
        nj = j+dy
        ans[ni][nj] = '#'
for i, j in [(0, 2), (2, 0)]:
    for dx, dy in dxy3:
        ni = i+dx
        nj = j+dy
        ans[ni][nj] = '#'
A = []
for i in range((N+1-6)//2):
    A.append((2*(i+1), 2*(i+1)+2))
for i, j in A:
    for dx, dy in dxy1:
        ni = i+dx
        nj = j+dy
        ans[ni][nj] = '#'
    for dx, dy in dxy2:
        ni = j+dx
        nj = i+dy
        ans[ni][nj] = '#'
if N % 2 == 0:
    # Nが偶数
    for i, j in [(N-4, N-2), (N-2, N-4)]:
        for dx, dy in dxy0:
            ni = i+dx
            nj = j+dy
            ans[ni][nj] = '#'
    for i, j in [(N-2, N-2)]:
        for dx, dy in dxy3:
            ni = i+dx
            nj = j+dy
            ans[ni][nj] = '#'
else:
    # Nが奇数
    ans[N-3][N-3] = '#'
    ans[N-3][N-1] = '#'
    ans[N-1][N-3] = '#'
    for i, j in [(N-2, N-2)]:
        for dx, dy in dxy3:
            ni = i+dx
            nj = j+dy
            ans[ni][nj] = '#'
for c in ans:
    print(*c, sep="")
