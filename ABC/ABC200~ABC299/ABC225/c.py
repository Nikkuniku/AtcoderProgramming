N, M = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(N)]
S = B[0][0]
d = S % 7
C = []
for i in range(N):
    tmp = []
    for j in range(min(M, 8 - d)):
        t = S + (7 * i) + j
        tmp.append(t)
        if t % 7 == 0:
            break
    C.append(tmp)
ans = "No"
if B == C:
    ans = "Yes"
print(ans)
