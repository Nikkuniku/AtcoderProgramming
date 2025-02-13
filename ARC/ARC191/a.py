N, M = map(int, input().split())
S = list(map(int, list(input())))
T = list(map(int, list(input())))
Ti = [(T[i], i) for i in range(M)]
Ti.sort(key=lambda x: x[1], reverse=True)
Ti.sort(reverse=True)
A = [False] * M
j = 0
for i in range(M):
    while j < N:
        if S[j] < Ti[i][0]:
            S[j] = Ti[i][0]
            A[Ti[i][1]] = True
            j += 1
            break
        else:
            j += 1
if not A[-1]:
    for i in range(N):
        if S[i] <= T[-1]:
            S[i] = T[-1]
            break
    else:
        S[-1] = T[-1]
print(*S, sep="")
