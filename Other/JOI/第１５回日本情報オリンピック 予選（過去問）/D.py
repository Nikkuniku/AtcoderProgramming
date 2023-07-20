from bisect import bisect_left
N, T, Q = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
Collision = []
for i in range(N-1):
    if A[i][1] == 1 and A[i+1][1] == 2:
        if abs(A[i+1][0]-A[i][0])//2 <= T:
            Collision.append((A[i+1][0]+A[i][0])//2)
M = len(Collision)
ans = []
for _ in range(Q):
    X = int(input())-1
    res = 0
    a, direction = A[X]
    idx = bisect_left(Collision, a)
    if direction == 1:
        if idx == M:
            res = a+T
        else:
            t = Collision[idx]
            res = min(a+T, t)
    elif direction == 2:
        if idx == 0:
            res = a-T
        else:
            t = Collision[idx-1]
            res = max(a-T, t)
    ans.append(res)
print(*ans, sep="\n")
