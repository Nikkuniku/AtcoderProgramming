def check(N, K, a, b, k):
    C = sorted([100 * a[i] - k * b[i] for i in range(N)], reverse=True)
    temp = sum(C[:K])
    return temp >= 0


N, K = map(int, input().split())
A, B = [], []
for _ in range(N):
    w, p = map(int, input().split())
    A.append(p * w)
    B.append(100 * w)
l = 0
r = 101
for _ in range(300):
    mid = (l + r) / 2
    if check(N, K, A, B, mid):
        l = mid
    else:
        r = mid
print(l)
