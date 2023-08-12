from collections import deque
N, L = map(int, input().split())
INF = 1 << 30
start = [INF]*N
time = [0]*N
q = deque()
A = [int(input()) for _ in range(N)]
dx = [-1, 1]
for i in range(N):
    isOK = True
    for d in dx:
        if not 0 <= i+d < N:
            continue
        if A[i] <= A[i+d]:
            isOK = False
    if isOK:
        q.append((i, 0))
while q:
    v, t = q.popleft()
    T = L-A[v]
    start[v] = t
    time[v] = T
    A[v] = 0
    for d in dx:
        j = v+d
        if not 0 <= j < N:
            continue
        isOK = True
        for dy in dx:
            if not 0 <= j+dy < N:
                continue
            if A[j] <= A[j+dy]:
                isOK = False
        if isOK:
            q.append((j, start[v]+T))
ans = max([start[i]+time[i] for i in range(N)])
print(ans)
