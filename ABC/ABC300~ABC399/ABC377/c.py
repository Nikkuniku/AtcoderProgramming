N, M = map(int, input().split())
ans = N * N
S = set()
dxy = [(-2, 1), (-1, 2), (1, 2), (2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
for _ in range(M):
    a, b = map(int, input().split())
    S.add((a, b))
    for dx, dy in dxy:
        if 1 <= a + dx <= N and 1 <= b + dy <= N:
            S.add((a + dx, b + dy))

ans -= len(S)
print(ans)
