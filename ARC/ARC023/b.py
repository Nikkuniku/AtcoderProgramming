R, C, D = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]
ans = 0
for r in range(R):
    for c in range(C):
        if r + c > D:
            continue
        if D % 2 == (r + c) % 2:
            ans = max(ans, A[r][c])
print(ans)
