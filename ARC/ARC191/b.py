def solve(N, K):
    digit_2 = []
    zeros = 0
    while N > 0:
        d = N % 2
        digit_2.append(d)
        N //= 2
        if d == 0:
            zeros += 1
    if (1 << zeros) < K:
        return -1
    b = list(bin(K - 1)[2:].zfill(zeros)[::-1])
    j = -1
    for i, v in enumerate(digit_2):
        if v == 0:
            j += 1
            digit_2[i] = int(b[j])
    res = 0
    for i, v in enumerate(digit_2):
        res += pow(2, i) * v
    return res


T = int(input())
ans = []
for _ in range(T):
    N, K = map(int, input().split())
    ans.append(solve(N, K))
print(*ans, sep="\n")
