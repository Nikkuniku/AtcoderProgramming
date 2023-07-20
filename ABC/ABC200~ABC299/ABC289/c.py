N, M = map(int, input().split())
C = []
for _ in range(M):
    c = int(input())
    C.append(list(map(int, input().split())))
ans = 0
for i in range(1 << M):
    s = set()
    for j in range(M):
        if i & (1 << j):
            for c in C[j]:
                s.add(c)

    if len(s) == N:
        ans += 1
print(ans)
