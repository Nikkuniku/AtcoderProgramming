N = int(input())
P = list(map(int, input().split()))
r = 1
Rank = [-1] * N
while 1:
    isEnd = True
    M = -1
    for i in range(N):
        if Rank[i] == -1:
            M = max(M, P[i])
            isEnd = False
    if isEnd:
        break
    k = 0
    for i in range(N):
        if P[i] == M:
            k += 1
            Rank[i] = r
    r += k
print(*Rank, sep="\n")
