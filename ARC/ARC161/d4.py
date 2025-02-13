N, D = map(int, input().split())
if N * D > N * (N - 1) // 2:
    exit(print("No"))
ans = []
if D == 1:
    # 数珠繋ぎ
    for i in range(N - 1):
        ans.append((i + 1, i + 2))
    if N > 2:
        ans.append((N, 1))
    print("Yes")
    for c in ans:
        print(*c)
elif N * D == N * (N - 1) // 2:
    # 完全グラフの場合
    for i in range(N):
        for j in range(i + 1, N):
            ans.append((i, j))
    print("Yes")
    for a, b in ans:
        print(a + 1, b + 1)
else:
    mods = [[] for _ in range(-(-N // (2 * D)))]
    for i in range(N):
        mods[i // (2 * D)].append(i)
    for k in range(-(-N // (2 * D))):
        M = len(mods[k])
        for p in range(M):
            for q in range(p + 1, M):
                a = mods[k][p]
                b = mods[k][q]
                ans.append((a, b))
                if len(ans) == N * D:
                    print("Yes")
                    for a, b in ans:
                        print(a + 1, b + 1)
                    exit()
    for k in range(1, -(-N // (2 * D))):
        L = len(mods[k - 1])
        M = len(mods[k])
        for p in range(M):
            for q in range(L):
                if p == q:
                    continue
                a = mods[k][p]
                b = mods[k - 1][q]
                ans.append((a, b))
                if len(ans) == N * D:
                    print("Yes")
                    for a, b in ans:
                        print(a + 1, b + 1)
                    exit()
