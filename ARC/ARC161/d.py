N, D = map(int, input().split())
if N * D > N * (N - 1) // 2:
    exit(print("No"))
ans = []
if D == 1:
    res = []
    for i in range(N - 1):
        res.append((i + 1, i + 2))
    if N > 2:
        res.append((N, 1))
    print("Yes")
    for c in res:
        print(*c)
    exit()
elif N * D == N * (N - 1) // 2:
    for i in range(N):
        for j in range(i + 1, N):
            ans.append((i + 1, j + 1))
else:
    for k in range(N):
        if k - 1 >= 2 * D:
            k -= 1
            break
    # k個で完全グラフの構築
    for i in range(k):
        for j in range(i + 1, k):
            ans.append((i + 1, j + 1))
    # 残りの頂点から、最初のk個にmaxk-1個の辺を張る
    cnt = k * (k - 1) // 2
    for i in range(k, N):
        for j in range(k - 1):
            if cnt < N * D:
                ans.append((i + 1, j + 1))
                cnt += 1
print("Yes")
for c in ans:
    print(*c)
