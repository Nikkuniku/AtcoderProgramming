from collections import defaultdict

N = int(input())
d = defaultdict(list)
for i in range(N):
    S = input()
    d[S].append(i + 1)
ans = []
for k in d.keys():
    tmp = 0
    for p in d[k]:
        tmp += p * (N - p + 1)
    ans.append((k, tmp))
ans.sort()
for k, v in ans:
    print(v, k)
