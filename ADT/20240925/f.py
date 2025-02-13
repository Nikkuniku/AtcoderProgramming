from itertools import accumulate

N = int(input())
A = list(map(int, input().split()))
X = int(input())
M = sum(A)
cum = list(accumulate(A, initial=0))
l = 0
r = 1 << 60
while r - l > 1:
    mid = (l + r) // 2
    K = mid // N
    tmp = K * M + cum[mid % N]
    if tmp <= X:
        l = mid
    else:
        r = mid
print(r)
