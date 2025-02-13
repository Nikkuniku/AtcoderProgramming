def mul_poly(f, g):
    h = [0] * (N + 1)
    for e1, c1 in enumerate(f):
        for e2 in g:
            e = e1 + e2
            if e > N:
                break
            h[e] += c1
    return h


from functools import reduce

MAX_N = 30000
N = MAX_N
fs = [range(0, N + 1, n) for n in range(1, N + 1)]
p = reduce(mul_poly, fs, [1])
print(p[N])
