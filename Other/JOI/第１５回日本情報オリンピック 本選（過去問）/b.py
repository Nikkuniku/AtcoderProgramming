from itertools import accumulate


def CS(S, T):
    n = len(S)
    status = {}
    for j in range(len(T)):
        status[j] = T[j]
    m = len(T)
    dp = [[0]*(n+1) for _ in range(m)]

    for j in range(m):
        for i in range(n):
            if j == 0:
                dp[j][i+1] = dp[j][i]
                if S[i] == status[j]:
                    dp[j][i+1] += 1
            else:
                dp[j][i+1] = dp[j][i]
                if S[i] == status[j]:
                    dp[j][i+1] += dp[j-1][i]

    return dp[m-1]


N = int(input())
S = input()
revS = S[::-1]
init = max(CS(S, 'JOI'))
Count_J = [0]*N
Count_I = [0]*N
for i in range(N):
    if S[i] == 'J':
        Count_J[i] += 1
    if S[N-1-i] == 'I':
        Count_I[i] += 1
CUM_J = list(accumulate([0]+Count_J))
CUM_I = list(accumulate([0]+Count_I))[::-1]
A = CS(S, 'JO')
B = CS(revS, 'IO')[::-1]
ans = 0
for i in range(N+1):
    tmp = []
    # when J
    tmp.append(B[i])
    # when O
    tmp.append(CUM_J[i]*CUM_I[i])
    # when I
    tmp.append(A[i])
    ans = max(ans, init+max(tmp))
print(ans)
