N, W = map(int, input().split())
A = list(map(int, input().split()))

l = 0
r = max(A) + 1
while r - l > 1:
    mid = (l + r) // 2
    needs = 0
    for a in A:
        needs += max(mid - a, 0)
    if needs <= W:
        l = mid
    else:
        r = mid
ans = max(A) - l
print(ans)
