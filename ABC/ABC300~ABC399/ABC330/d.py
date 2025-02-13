N = int(input())
S = [list(input()) for _ in range(N)]
row = [[] for _ in range(N)]
col = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if S[i][j] == "o":
            row[i].append(j)
for j in range(N):
    for i in range(N):
        if S[i][j] == "o":
            col[j].append(i)
ans = 0
for i in range(N):
    for j in range(N):
        if S[i][j] != "o":
            continue
        p = len(col[j]) - 1
        q = len(row[i]) - 1
        ans += p * q
print(ans)
