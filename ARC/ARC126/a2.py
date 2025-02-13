def solve(t2, t3, t4):
    t6 = t3 // 2
    res = 0
    a = min(t6, t4)
    res += a
    t6 -= a
    t4 -= a
    b = min(t6, t2 // 2)
    res += b
    t2 -= 2 * b
    c = min(t4 // 2, t2)
    res += c
    t4 -= 2 * c
    t2 -= c
    d = min(t4, t2 // 3)
    res += d
    t2 -= 3 * d
    res += t2 // 5
    return res


T = int(input())
ans = [solve(*map(int, input().split())) for _ in range(T)]
print(*ans, sep="\n")
