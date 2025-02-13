N, M = map(int, input().split())
used = set()
for _ in range(M):
    a, b = map(int, input().split())
    used.add((a + b) % N)
k = 0
while len(used) < M:
    if k not in used:
        used.add(k)
    k += 1
ans = []
for s in used:
    for i in range(N):
        j = (s - (i + 2)) % N
        ans.append((i + 1, j + 1))
print(len(ans))
for c in ans:
    print(*c)
