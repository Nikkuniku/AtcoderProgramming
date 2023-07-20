from collections import defaultdict
X = input()
d = defaultdict(int)
for i in range(len(X)):
    d[X[i]] = chr(97+i)
N = int(input())
S = [input() for _ in range(N)]
S_conv = []
for i in range(N):
    tmp = []
    for j in range(len(S[i])):
        tmp.append(d[S[i][j]])
    S_conv.append([''.join(tmp), i])
S_conv.sort(key=lambda x: x[0])
ans = []
for i in range(len(S_conv)):
    ans.append(S[S_conv[i][1]])
print(*ans, sep="\n")
