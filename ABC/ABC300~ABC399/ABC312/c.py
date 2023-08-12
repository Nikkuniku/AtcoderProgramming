N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
l = 0
r = 1 << 30


def sell(k):
    res = 0
    for a in A:
        if k >= a:
            res += 1
    return res


def buy(k):
    res = 0
    for b in B:
        if k <= b:
            res += 1
    return res


while r-l > 1:
    mid = (l+r)//2
    P = sell(mid)
    Q = buy(mid)
    if P >= Q:
        r = mid
    else:
        l = mid
ans = r
print(r)
