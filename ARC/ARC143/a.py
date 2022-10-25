s = list(map(int, input().split()))
s.sort()
a, b, c = s[0], s[1], s[2]
ans = -1
if a >= c-b:
    ans = c
print(ans)
