from bisect import bisect_left, bisect_right
from string import ascii_uppercase

S = input()
P = [[] for _ in range(26)]
for i in range(len(S)):
    j = ascii_uppercase.index(S[i])
    P[j].append(i)
ans = 0
for i in range(len(S)):
    for j in range(26):
        a = bisect_left(P[j], i)
        b = bisect_right(P[j], i)
        ans += a * (len(P[j]) - b)
print(ans)
