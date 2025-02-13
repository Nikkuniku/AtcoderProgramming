N = int(input())
M = int(input())
G = [[0] * N for i in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a][b] = 1
for c in G:
    print(*c, sep="")
