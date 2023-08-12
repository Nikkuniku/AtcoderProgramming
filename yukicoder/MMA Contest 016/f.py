S = input()
N = len(S)
alp = [[] for _ in range(26)]
ans = 0
for i, v in enumerate(S):
    alp[ord(v)-65].append(i)
for i in range(26):
    for j in range(1, len(alp[i])):
        idx = alp[i][j]
        tmp = j*(N-idx-1-(len(alp[i])-j-1))
        ans += tmp
print(ans)
