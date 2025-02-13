from collections import defaultdict

N = int(input())
S = [list(input()) for _ in range(N)]

R = [defaultdict(int) for _ in range(N)]
C = [defaultdict(int) for _ in range(N)]
for i in range(N):
    for j in range(N):
        R[i][S[i][j]] += 1
for j in range(N):
    for i in range(N):
        C[j][S[i][j]] += 1
Right = defaultdict(int)
Left = defaultdict(int)
for i in range(N):
    Right[S[i][i]] += 1
    Left[S[N - 1 - i][i]] += 1

ans = 0
for i in range(N):
    for j in range(N):
        if S[i][j] != ".":
            continue
        if R[i]["A"] == N - 1:
            ans += 1
        if C[j]["A"] == N - 1:
            ans += 1
        if i == j and Right["A"] == N - 1:
            ans += 1
        if i + j == N - 1 and Left["A"] == N - 1:
            ans += 1
print(ans)
