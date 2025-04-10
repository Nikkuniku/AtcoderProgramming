N, X = map(int, input().split())
U = []
D = []
P = []
for _ in range(N):
    u, d = map(int, input().split())
    U.append(u)
    D.append(d)
    P.append(u + d)
H = min(P)


def check(N, U, D, H, X):
    for i in range(N):
        a = H - D[i]
        b = U[i]
        if a > b:
            return False
        if i == 0:
            preL = a
            preR = b
        else:
            if not max(preL - X, a) <= min(preR + X, b):
                return False
            preL = max(preL - X, a)
            preR = min(preR + X, b)
    return True


def calc_cost(P, H):
    return sum(P) - len(P) * H


l, r = 0, 1 << 60
while r - l > 1:
    mid = (l + r) // 2
    if check(N, U, D, mid, X):
        l = mid
    else:
        r = mid
print(calc_cost(P, l))
