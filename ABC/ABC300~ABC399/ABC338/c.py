N = int(input())
Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
MaxA = 1 << 60
MaxB = 1 << 60
for i, a in enumerate(A):
    if a == 0:
        continue
    tmp = Q[i] // a
    MaxA = min(MaxA, tmp)
for j, b in enumerate(B):
    if b == 0:
        continue
    MaxB = min(MaxB, Q[j] // b)
ans = []
for k in range(MaxA + 1):
    P = []
    isOK = True
    for i in range(N):
        if Q[i] - A[i] * k < 0:
            isOK = False
            break
        P.append(Q[i] - A[i] * k)
    if not isOK:
        continue
    T = []
    for i in range(N):
        if B[i] == 0:
            continue
        T.append(P[i] // B[i])
    ans.append(k + min(T))
print(max(ans))
