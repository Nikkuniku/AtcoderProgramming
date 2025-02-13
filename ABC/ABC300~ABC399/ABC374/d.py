from itertools import permutations


def dist(X, Y):
    return ((X[0] - Y[0]) ** 2 + (X[1] - Y[1]) ** 2) ** 0.5


N, S, T = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(N)]
P = list(permutations(range(N)))
ans = 1e18
for per in P:
    for s in range(1 << N):
        sx, sy = 0, 0
        direction = []
        tmp = 0
        for i in range(N):
            if s & (1 << i):
                direction.append(1)
            else:
                direction.append(0)
        for j in range(N):
            a = L[per[j]][:2]
            b = L[per[j]][2:]
            if direction[per[j]] == 1:
                tmp += dist([sx, sy], a) / S
                sx, sy = b
            else:
                tmp += dist([sx, sy], b) / S
                sx, sy = a
            tmp += dist(a, b) / T
        ans = min(ans, tmp)
print(ans)
