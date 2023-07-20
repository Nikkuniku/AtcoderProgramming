from collections import defaultdict
S = input()
N = len(S)
d = defaultdict(int)
cnts = [[0] for _ in range(10)]
for i in range(N):
    for j in range(10):
        cnts[j].append(cnts[j][-1]+(j == int(S[i])))
for i in range(N+1):
    tmp = []
    for j in range(10):
        tmp.append(str(cnts[j][i] % 2))
    d[''.join(tmp)] += 1
ans = 0
for k, v in d.items():
    ans += v*(v-1)//2
print(ans)
