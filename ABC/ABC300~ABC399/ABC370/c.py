S = list(input())
T = list(input())
L = []
R = []
for i in range(len(S)):
    if S[i] == T[i]:
        continue
    if S[i] < T[i]:
        R.append(i)
    else:
        L.append(i)
ans = []
for i in L:
    tmp = S[:]
    tmp[i] = T[i]
    ans.append("".join(tmp))
    S = tmp
for i in reversed(R):
    tmp = S[:]
    tmp[i] = T[i]
    ans.append("".join(tmp))
    S = tmp
print(len(ans))
print(*ans, sep="\n")
