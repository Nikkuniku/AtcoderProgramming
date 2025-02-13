N = int(input())
A = [1, 1, 1]
B = [0, 0, 0]
kukan = [-(1 << 60), 1 << 60]
for _ in range(N):
    a, t = map(int, input().split())
    L, R = kukan[0], kukan[1]
    if t == 1:
        for i in range(3):
            B[i] += a
    elif t == 2:
        if L + B[0] <= a:
            kukan[0] = a - B[1]
            A[0] = 0
            B[0] = a
        if R + B[1] <= a:
            kukan[1] = a - B[1]
            A[1] = 0
            B[1] = a
        if R + B[2] <= a:
            A[2] = 0
            B[2] = a
    elif t == 3:
        if R + B[2] >= a:
            kukan[1] = a - B[1]
            A[2] = 0
            B[2] = a
        if L + B[1] >= a:
            kukan[1] = a - B[1]
            A[1] = 0
            B[1] = a
        if L + B[0] >= a:
            A[0] = 0
            B[0] = a


Q = int(input())
X = list(map(int, input().split()))
ans = []
for x in X:
    if x < kukan[0]:
        tmp = A[0] * x + B[0]
    elif kukan[0] <= x < kukan[1]:
        tmp = A[1] * x + B[1]
    else:
        tmp = A[2] * x + B[2]
    ans.append(tmp)
print(*ans, sep="\n")
