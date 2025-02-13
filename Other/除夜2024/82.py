N = int(input())
M = -1
S = []
for _ in range(N):
    s = input()
    S.append(s)
    M = max(M, len(s))
ans = [[] for _ in range(M)]
for i in range(N):
    for j in range(M):
        if j > len(S[i]) - 1:
            ans[j].append("*")
        else:
            ans[j].append(S[i][j])
for c in ans:
    c = c[::-1]
    while c[-1] == "*":
        c.pop()
    print(*c, sep="")
