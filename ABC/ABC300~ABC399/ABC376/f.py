from collections import defaultdict

N, Q = map(int, input().split())
INF = 1e18
dp = [[INF, INF] for _ in range(Q + 1)]
dp[0] = [0, 0]
d = defaultdict(list)
d[0, 0].append((0, 1))
d[0, 1].append((0, 1))
for i in range(Q):
    H, T = input().split()
    T = int(T) - 1
    if H == "L":
        for j in range(2):
            # 左回り
            for L, R in d[i, j]:
                tmp_left = 0
                isover = False
                while L != T:
                    L = (L - 1) % N
                    tmp_left += 1
                    if L == R:
                        isover = True
                if isover:
                    while R != (T - 1) % N:
                        R = (R - 1) % N
                        tmp_left += 1
                if tmp_left + dp[i][j] <= dp[i + 1][0]:
                    dp[i + 1][0] = tmp_left + dp[i][j]
                    d[i + 1, 0].append((L, R))
            # 右回り
            for L, R in d[i, j]:
                tmp_right = 0
                isover = False
                while L != T:
                    L = (L + 1) % N
                    tmp_right += 1
                    if L == R:
                        isover = True
                if isover:
                    while R != (T + 1) % N:
                        R = (R + 1) % N
                        tmp_right += 1
                if tmp_right + dp[i][j] <= dp[i + 1][1]:
                    dp[i + 1][1] = tmp_right + dp[i][j]
                    d[i + 1, 1].append((L, R))
    elif H == "R":
        for j in range(2):
            # 左回り
            for L, R in d[i, j]:
                tmp_left = 0
                isover = False
                while R != T:
                    R = (R - 1) % N
                    tmp_left += 1
                    if R == L:
                        isover = True
                if isover:
                    while L != (T - 1) % N:
                        L = (L - 1) % N
                        tmp_left += 1
                if tmp_left + dp[i][j] <= dp[i + 1][0]:
                    dp[i + 1][0] = tmp_left + dp[i][j]
                    d[i + 1, 0].append((L, R))
            # 右回り
            for L, R in d[i, j]:
                tmp_right = 0
                isover = False
                while R != T:
                    R = (R + 1) % N
                    tmp_right += 1
                    if R == L:
                        isover = True
                if isover:
                    while L != (T + 1) % N:
                        L = (L + 1) % N
                        tmp_right += 1
                if tmp_right + dp[i][j] <= dp[i + 1][1]:
                    dp[i + 1][1] = tmp_right + dp[i][j]
                    d[i + 1, 1].append((L, R))
ans = min(dp[Q])
print(ans)
