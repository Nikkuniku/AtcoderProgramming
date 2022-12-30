N, K = map(int, input().split())
A = sorted(list(map(int, input().split())),reverse=True)
F = sorted(list(map(int, input().split())))
l,r = -1,1<<40
while r-l > 1:
    mid = (l+r)//2
    TrainCount = sum([max(A[i]-(mid//F[i]), 0) for i in range(N)])
    if TrainCount <= K:
        r = mid
    else:
        l = mid
print(r)
