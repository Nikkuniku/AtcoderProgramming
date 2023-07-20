from itertools import permutations
N, M = map(int, input().split())
S = [input() for _ in range(N)]
P = list(permutations(S))
ans = 'No'
for p in P:
    isOK = True
    for i in range(len(p)-1):
        A = p[i]
        B = p[i+1]
        diff = 0
        for j in range(M):
            if A[j] != B[j]:
                diff += 1
        if diff != 1:
            isOK = False
    if isOK:
        ans = 'Yes'
print(ans)
