N = int(input())
Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
L = 1000002
ans = 0
for i in range(L):
    isOK = True
    C = Q[:]
    for j in range(N):
        if A[j] * i > C[j]:
            isOK = False
            break
        C[j] -= A[j] * i
    if not isOK:
        continue
    D = []
    for j in range(N):
        if B[j] == 0:
            continue
        D.append(C[j] // B[j])
    ans = max(ans, i + min(D))
print(ans)
