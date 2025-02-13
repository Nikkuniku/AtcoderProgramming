X, Y, A, B, C = map(int, input().split())
if A + B + C > X * Y:
    exit(print("No"))


def f(S, T, P):
    l = 0
    r = S + 1
    while r - l > 1:
        mid = (l + r) // 2
        if P <= mid * T:
            r = mid
        else:
            l = mid
    return r


ans = "No"
Q = [(A, B, C), (B, A, C), (C, A, B)]
R = [(X, Y), (Y, X)]
# 「に」の置き方
for p, q, r in Q:
    for s, t in R:
        x1 = f(s, t, p)
        if p <= t * x1 and 0 < x1 <= s:
            z = f(t, s - x1, q)
            if q <= (s - x1) * z and r <= (s - x1) * (t - z) and z <= t:
                ans = "Yes"
# 「川」の置き方
for s, t in R:
    x1 = f(s, t, A)
    if A <= t * x1 and 0 < x1 <= s:
        x2 = f(s - x1, t, B)
        if x2 <= s - x1 and B <= t * x2 and C <= t * (s - x1 - x2):
            ans = "Yes"
print(ans)
