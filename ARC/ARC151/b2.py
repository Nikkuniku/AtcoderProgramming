N, M = map(int, input().split())
P = list(map(int, input().split()))
ans = 0
for i in range(1, M+1):
    for j in range(1, M+1):
        for k in range(1, M+1):
            for l in range(1, M+1):
                for p in range(1, M+1):
                    A = [str(i), str(j), str(k), str(l), str(p)]
                    B = [0]*N
                    for m in range(N):
                        B[P.index(m+1)] = A[m]
                    tmpa = ''.join(A)
                    tmpb = ''.join(B)
                    if tmpa < tmpb:
                        ans += 1
print(ans)
