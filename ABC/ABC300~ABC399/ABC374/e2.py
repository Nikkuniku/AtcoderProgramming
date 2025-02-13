N, X = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(N)]


def check(k):
    temp = 0
    for i in range(N):
        a, p, b, q = C[i]
        cost = 1 << 60
        for x in range(101):
            if k - a * x + b - 1 >= 0:
                y = (k - a * x + b - 1) // b
                cost = min(cost, p * x + q * y)
        for y in range(101):
            if k - b * y + a - 1 >= 0:
                x = (k - b * y + a - 1) // a
                cost = min(cost, p * x + q * y)
        temp += cost
    return temp <= X


l = 0
r = 1 << 30
while r - l > 1:
    mid = (l + r) // 2
    if check(mid):
        l = mid
    else:
        r = mid
print(l)
