def solve(a, b):
    l = 1
    r = 64000
    P = 4*a*b
    while r-l > 1:
        mid = (l+r)//2
        Q = mid*mid - a - b
        R = Q**2
        if Q > 0:
            if P < R:
                r = mid
            else:
                l = mid
        else:
            l = mid
    return r


N = int(input())
ans = []
for _ in range(N):
    A, B = map(int, input().split())
    ans.append(solve(A, B))
print(*ans, sep="\n")
