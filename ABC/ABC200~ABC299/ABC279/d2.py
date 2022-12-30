A, B = map(int, input().split())


def f(k):
    return pow(A, 2) - 4*pow(B, 2)*((1+k)**3)


def g(k):
    return B*k + A/((1+k)**(1/2))


l = 0
r = 1 << 80
while r-l > 1:
    mid = (l+r)//2
    if f(mid) > 0:
        l = mid
    else:
        r = mid


ans = min(g(l), g(r))
print(ans)
