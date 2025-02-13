N, M, K = map(int, input().split())
P = [list(input().split()) for _ in range(M)]
ans = 0
for i in range(1 << N):
    isOK = True
    for j in range(M):
        C = int(P[j][0])
        cnt = 0
        for k in range(1, C + 1):
            tmp = int(P[j][k]) - 1
            if i & (1 << tmp):
                cnt += 1
        res = P[j][-1]
        if not ((cnt >= K and res == "o") or (cnt < K and res == "x")):
            isOK = False
    if isOK:
        ans += 1
print(ans)
