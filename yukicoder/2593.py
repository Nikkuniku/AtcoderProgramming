from collections import Counter, defaultdict

N = int(input())
S = input()
ans = set()
C_S = Counter(S)
for i in range(1000):
    isOK = True
    d = defaultdict(int)
    for t in list(str(i).zfill(min(3, N))):
        d[t] += 1
    for k, v in d.items():
        if C_S[k] < v:
            isOK = False
    if isOK:
        ans.add(i % 40)
print(len(ans))
