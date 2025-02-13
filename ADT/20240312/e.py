N = int(input())
Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
minA = 1 << 60
for a in A:
    if a > 0:
        minA = min(a, minA)
K = max(Q) // minA

ans = 0
for k in range(K + 1):
    tmp = []
    isOK = True
    for i in range(N):
        if Q[i] >= A[i] * k:
            tmp.append(Q[i] - A[i] * k)
        else:
            isOK = False
            break
    if not isOK:
        continue
    cnt = 1 << 60
    for j in range(N):
        if tmp[j] < B[j]:
            isOK = False
            break
        if B[j] == 0:
            continue
        cnt = min(cnt, tmp[j] // B[j])
    if not isOK:
        continue
    ans = max(ans, k + cnt)
print(ans)
