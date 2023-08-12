def solve(N, K):
    j = N-1
    ans = []
    while 1:
        if j == -1:
            ans.append('J')
            break
        if K <= 2**j:
            for _ in range(2**j):
                ans.append('J')
            for _ in range(2**j):
                ans.append('O')
            break
        else:
            for _ in range(2**j):
                ans.append('I')
            K -= pow(2, j)
            j -= 1
    return ''.join(ans)


N, K = map(int, input().split())

print(solve(N, K))
