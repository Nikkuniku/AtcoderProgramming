n = int(input())
s = list(input())
t = list(input())

a_s = []
a_t = []

for i in range(n):
    if s[i] == '0':
        a_s.append(i)
    if t[i] == '0':
        a_t.append(i)
if len(a_s) != len(a_t):
    ans = -1
else:
    ans = 0
    for j in range(len(a_s)):
        if a_s[j] != a_t[j]:
            ans += 1

print(ans)
