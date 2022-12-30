N, M = map(int, input().split())
INF = 10**10
cake = [tuple(map(int, input().split())) for _ in range(N)]

ans = []
for i in range(1 << 3):
    tmp = []
    for j in range(N):
        t = 0
        for k in range(3):
            if i & (1 << k):
                t += cake[j][k]
            else:
                t -= cake[j][k]
        tmp.append(t)
    tmp.sort(reverse=True)
    ans.append(sum(tmp[:M]))

print(max(ans))
