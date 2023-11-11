N, Q = map(int, input().split())
P = [i+1 for i in range(N)]
pos = [-1+i for i in range(N+1)]
for _ in range(Q):
    x = int(input())
    i = pos[x]
    if i == N-1:
        y = P[i-1]
    else:
        y = P[i+1]
    j = pos[y]
    P[i], P[j] = P[j], P[i]
    pos[x], pos[y] = pos[y], pos[x]
print(*P)
