def solve(n, k):
    S = []
    while n:
        S.append(n % 3)
        n //= 3
    P = sum(S)
    if P <= K and P % 2 == k % 2:
        return True
    return False


T = int(input())
ans = []
for _ in range(T):
    res = 'No'
    N, K = map(int, input().split())
    if solve(N, K):
        res = 'Yes'
    ans.append(res)
print(*ans, sep="\n")
