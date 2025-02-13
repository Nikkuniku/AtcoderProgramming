N, Q = map(int, input().split())
Ball = [i + 1 for i in range(N)]
pos = [i - 1 for i in range(N + 1)]
for _ in range(Q):
    x = int(input())
    i = pos[x]
    if i == N - 1:
        y = Ball[i - 1]
    else:
        y = Ball[i + 1]
    j = pos[y]
    Ball[i], Ball[j] = Ball[j], Ball[i]
    pos[x], pos[y] = j, i
print(*Ball)
