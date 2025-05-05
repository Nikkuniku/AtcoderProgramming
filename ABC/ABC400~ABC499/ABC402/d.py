N, M = map(int, input().split())
mods = [0] * N
for _ in range(M):
    a, b = map(int, input().split())
    mods[(a + b - 2) % N] += 1
ans = M * (M - 1) // 2
for i in range(N):
    ans -= mods[i] * (mods[i] - 1) // 2
print(ans)
