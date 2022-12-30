n = int(input())
s = []
for _ in range(2):
    s.append(list(input()))


i = 0
ans = 1
MOD = pow(10, 9)+7
pre = -1
# first
if s[0][i] == s[1][i]:
    ans *= 3
    i += 1
    pre = 1
else:
    ans *= 6
    i += 2
    pre = 2

while i < n:
    if s[0][i] == s[1][i]:
        if pre == 1:
            ans *= 2
        else:
            ans *= 1
        i += 1
        pre = 1
    else:
        if pre == 1:
            ans *= 2
        else:
            ans *= 3
        i += 2
        pre = 2
    ans %= MOD
print(ans)
