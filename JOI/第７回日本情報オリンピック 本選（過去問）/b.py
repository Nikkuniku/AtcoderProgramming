def solve(S, T):
    dp0 = [0]*(len(T)+1)
    dp1 = [0]*(len(T)+1)
    res = 0
    for i in range(len(S)):
        for j in range(len(T)):
            if S[i] == T[j]:
                dp1[j+1] = dp0[j]+1
            else:
                dp1[j+1] = 0
        res = max(res, max(dp1))
        dp1, dp0 = dp0, dp1
    return res


ans = []
while True:
    try:
        S = input()
        T = input()
        ans.append(solve(S, T))
    except EOFError:
        break
print(*ans, sep="\n")
