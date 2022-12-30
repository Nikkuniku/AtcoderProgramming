from collections import defaultdict
s = input()
n = len(s)
ans = 0
d = defaultdict(int)
d[0] = 1
tmp = 0
for i in range(n):
    tmp += int(s[n-1-i])*pow(10, i, 2019)
    tmp %= 2019
    ans += d[tmp]
    d[tmp] += 1
print(ans)
