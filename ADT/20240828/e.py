N, M = map(int, input().split())
A = list(map(int, input().split()))
P = [0] * N
S = [list(input()) for _ in range(N)]
for i in range(N):
    tmp = 0
    for j, v in enumerate(S[i]):
        if v == "o":
            tmp += A[j]
    P[i] = tmp + i + 1
K = max(P)
cnt = P.count(K)
ans = []
for i in range(N):
    tmp = []
    for j in range(M):
        if S[i][j] == "x":
            tmp.append(A[j])
    tmp.sort()
    tmp = tmp[::-1]
    score = P[i]
    if score == K and cnt == 1:
        ans.append(0)
        continue
    for k in range(len(tmp)):
        score += tmp[k]
        if score >= K:
            ans.append(k + 1)
            break
print(*ans, sep="\n")
