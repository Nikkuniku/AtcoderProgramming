from collections import Counter
n, m = map(int, input().split())
s = list(input().split())
t = list(input().split())

# 可能か判定

c = Counter(t)
for v in c.keys():
    if v not in s:
        print(-1)
        exit(0)

a = s[0]
shift = []
for i in range(1, n):
    if s[i] != a:
        shift.append(i)
        break
for i in range(n-1, -1, -1):
    if s[i] != a:
        shift.append(n-i)
        break
if not shift:
    shift.append(0)
minshift = min(shift)

Flg = False
ans = 0
for i in range(m):
    if t[i] != a:
        if Flg:
            ans += 2
        else:
            Flg = True
            ans += minshift+1
    else:
        ans += 1
    a = t[i]
print(ans)
