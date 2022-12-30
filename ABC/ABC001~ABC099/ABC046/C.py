N = int(input())


def f(t, a, ti, ai):
    l = 0
    r = 1 << 60
    while r-l > 1:
        mid = (l+r)//2
        if t <= ti*mid and a <= ai*mid:
            r = mid
        else:
            l = mid
    return r


x, y = 1, 1
for _ in range(N):
    ti, ai = map(int, input().split())
    k = f(x, y, ti, ai)
    x, y = ti*k, ai*k
print(x+y)
