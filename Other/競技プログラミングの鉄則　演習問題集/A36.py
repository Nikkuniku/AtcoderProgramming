N, K = map(int, input().split())
dist = 2 * (N - 1)
ans = "Yes" if K % 2 == 0 and dist <= K else "No"
print(ans)
