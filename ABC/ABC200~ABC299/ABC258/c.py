n, q = map(int, input().split())
s = input()
c = 0
ans = []
for _ in range(q):
    t, x = map(int, input().split())
    if t == 1:
        c += x
        x %= n
    else:
        y = (x-c) % n
        ans.append(s[y-1])

print(*ans, sep="\n")
