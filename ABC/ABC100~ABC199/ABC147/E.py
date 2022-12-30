H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]
AB = [[0]*W for _ in range(H)]
for h in range(H):
    for w in range(W):
        AB[h][w] = abs(A[h][w]-B[h][w])
dp = [[set() for _ in range(W)] for _ in range(H)]
dp[0][0].add(AB[0][0])
for h in range(H):
    if h == 0:
        for w in range(1, W):
            for f in dp[h][w-1]:
                dp[h][w].add(f+AB[h][w])
                dp[h][w].add(abs(f-AB[h][w]))
    else:
        for w in range(W):
            if w-1 >= 0:
                for f in (dp[h-1][w] | dp[h][w-1]):
                    dp[h][w].add(f+AB[h][w])
                    dp[h][w].add(abs(f-AB[h][w]))
            else:
                for f in dp[h-1][w]:
                    dp[h][w].add(f+AB[h][w])
                    dp[h][w].add(abs(f-AB[h][w]))

ans = 1 << 20
for s in dp[H-1][W-1]:
    ans = min(ans, abs(s))
print(ans)
