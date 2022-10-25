n = int(input())
ans = 0
re = []
for _ in range(n):
    t, a = input().split()
    a = int(a)
    if t == '+':
        ans += a
    elif t == '-':
        ans -= a
    else:
        ans *= a
    ans %= 10000
    re.append(ans)
print(*re, sep="\n")
