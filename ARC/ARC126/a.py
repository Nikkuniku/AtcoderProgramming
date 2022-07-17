
def solve(a, b, c):
    k = b//2
    ans = 0
    if c >= k:
        b -= 2*k
        c -= k
        ans += k
    else:
        # c<kのとき
        if a >= 2*(k-c):
            a -= 2*(k-c)
            c = k
        else:
            # a<2*(k-c)のとき
            c += a//2
            a %= 2
        ans += min(c, b//2)
        b, c = b-2*min(c, b//2), c-min(c, b//2)

    k = c//2
    if a >= k:
        c -= 2*k
        a -= k
        ans += k
    if a >= 3*c:
        a -= 3*c
        ans += c
        c = 0
    ans += a//5
    return ans


t = int(input())
ans = []
for _ in range(t):
    a, b, c = map(int, input().split())
    ans.append(solve(a, b, c))
print(*ans, sep="\n")
