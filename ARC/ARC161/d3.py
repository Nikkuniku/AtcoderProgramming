N, D = map(int, input().split())
if N * D > N * (N - 1) // 2:
    exit(print("No"))
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
Edges = set()
kouho = set()
for i in range(N):
    for j in range(i + 1, N):
        Edges.add((i + 1, j + 1))
for k in range(2 * D + 1, N):
    mods = [[] for _ in range(k - 1)]
    for i in range(N):
        mods[i % (k - 1)].append(i)
    for j in range(k - 1):
        for p in range(len(mods[j])):
            for q in range(p + 1, len(mods[j])):
                a, b = mods[j][p], mods[j][q]
                if b < a:
                    a, b = b, a
                kouho.add((a + 1, b + 1))
Edges -= kouho
M = len(Edges)
if M >= N * D:
    Edges = list(Edges)
    for _ in range(M - N * D):
        Edges.pop()
else:
    exit(print("No"))
print("Yes")
for c in Edges:
    print(*c)
