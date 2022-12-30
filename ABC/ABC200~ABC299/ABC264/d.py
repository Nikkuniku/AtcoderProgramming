s = list(input())
t = 'atcoder'

ans = 0
for i in range(len(s)):
    if s[i] == t[i]:
        continue
    idx = s.index(t[i])
    ans += idx-i
    while s[i] != t[i]:
        s[idx-1], s[idx] = s[idx], s[idx-1]
        idx -= 1

print(ans)
