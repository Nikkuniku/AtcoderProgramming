def solve(n):
    k = 1
    repunit = 1
    while 1:
        if repunit % n == 0:
            break
        repunit *= 10
        repunit += 1
        repunit %= n
        k += 1
    return k


from math import gcd

N = 1000000
for n in range(N, 2 * N):
    if gcd(n, 10) != 1:
        continue
    res = solve(n)
    if res >= 1000000:
        print("A({})={}".format(n, res))
        break
    # print("R({})".format(k), n, "A({})={}".format(n, k))
