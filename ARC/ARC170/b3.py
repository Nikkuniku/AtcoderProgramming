N = int(input())
A = list(map(int, input().split()))
M = 10

ans = N * (N - 1) // 2
for l in range(N):
    for r in range(l + 1, min(l + 2 * M + 1, N)):
        kouho = set()
        Subset = set()
        isBad = True
        for k in range(r - l + 1):
            s = l + k
            if A[s] in kouho:
                isBad = False
                break
            for b in Subset:
                d = A[s] - b
                kouho.add(A[s] + d)
            Subset.add(A[s])
        if isBad:
            ans -= 1
print(ans)
