
N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]


def comb(a, b):
    return a*(a-1)*(a-2)//6


def solve(p, q, r):
    a, b = p
    c, d = q
    e, f = r
    dx1 = c-a
    dx2 = e-a
    dy1 = d-b
    dy2 = f-b
    return dx2*dy1 == dx1*dy2


ans = set()
for i in range(N):
    for j in range(i+1, N):
        tmp = [i, j]
        for k in range(N):
            if k == i or k == j:
                continue
            X = points[i]
            Y = points[j]
            Z = points[k]
            if solve(X, Y, Z):
                tmp.append(k)
        ans.add(tuple(sorted(tmp)))
res = comb(N, 3)
for c in ans:
    res -= comb(len(c), 3)
print(res)
