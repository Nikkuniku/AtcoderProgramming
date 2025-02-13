N, M = map(int, input().split())
A = list(map(int, input().split()))
if sum(A) <= M:
    exit(print("infinite"))


def check(k, A):
    res = 0
    for a in A:
        res += min(a, k)
    return res


l = 0
r = 1 << 60
while r - l > 1:
    mid = (l + r) // 2
    if check(mid, A) <= M:
        l = mid
    else:
        r = mid
print(l)
