from collections import defaultdict

N = int(input())
d = defaultdict(int)
ans = []
for _ in range(N):
    s = input()
    if d[s]:
        ans.append(s + "(" + str(d[s]) + ")")
    else:
        ans.append(s)
    d[s] += 1
print(*ans, sep="\n")
