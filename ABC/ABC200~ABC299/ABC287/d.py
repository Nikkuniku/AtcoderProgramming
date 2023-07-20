S = input()
T = input()
N = len(S)
M = len(T)
ans = []
nonmatch = 0
ok = [True]*M
for i in range(M):
    s = S[N-M+i]
    t = T[i]
    if (s == t) or s == '?' or t == '?':
        continue
    nonmatch += 1
    ok[i] = False
if nonmatch > 0:
    ans.append('No')
else:
    ans.append('Yes')
for i in range(M):
    s = S[i]
    t = T[i]
    if (s == t) or s == '?' or t == '?':
        if not ok[i]:
            nonmatch -= 1
    else:
        nonmatch += 1
    if nonmatch > 0:
        ans.append('No')
    else:
        ans.append('Yes')
print(*ans, sep="\n")
