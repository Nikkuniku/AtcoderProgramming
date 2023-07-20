def solve(x):
    res = 0
    k = 2
    for k in range(2, min(x, 51)):
        M = x-(k*(k-1)//2)
        if M % k == 0 and M//k > 0:
            res += 1
        k += 1
    return res


ans = []
while 1:
    N = int(input())
    if N == 0:
        break
    ans.append(solve(N))
print(*ans, sep="\n")
