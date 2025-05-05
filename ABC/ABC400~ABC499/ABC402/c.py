N, M = map(int, input().split())
foods = [[] for _ in range(N + 1)]
dislikes = []
ans = []
res = 0
for i in range(M):
    K, *A = list(map(int, input().split()))
    dislikes.append(K)
    for a in A:
        foods[a].append(i)
B = list(map(int, input().split()))
for b in B:
    for f in foods[b]:
        dislikes[f] -= 1
        if dislikes[f] == 0:
            res += 1
    ans.append(res)
print(*ans, sep="\n")
