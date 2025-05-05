T = input()
U = input()
N = len(T)
M = len(U)
ans = "No"
for i in range(N - M + 1):
    isOK = True
    for j in range(M):
        if T[i + j] != "?" and T[i + j] != U[j]:
            isOK = False
    if isOK:
        ans = "Yes"
print(ans)
