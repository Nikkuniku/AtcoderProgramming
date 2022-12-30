N, M = map(int, input().split())
deg = [0]*N
for _ in range(M):
    a, b = map(lambda x: int(x)-1, input().split())
    deg[a] += 1
    deg[b] += 1
print(*deg, sep="\n")
