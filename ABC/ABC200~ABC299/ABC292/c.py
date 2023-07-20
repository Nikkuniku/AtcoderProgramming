def solve(M):
    res = 0
    for i in range(1, M+1):
        if i**2 > M:
            break
        if M % i == 0:
            if i != M//i:
                res += 2
            else:
                res += 1
    return res


N = int(input())
ans = 0
for i in range(1, N):
    AB = i
    CD = N-i
    ans += solve(AB)*solve(CD)
print(ans)
