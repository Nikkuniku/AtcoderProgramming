

n = int(input())
a = list(map(int, input().split()))

ans = -10**8
ans_t = -10**8
for i in range(n-1):
    ans_a = -10**8
    for j in range(i+1, n):

        takahashi = 0
        aoki = 0
        for k in range(j-i+1):
            p = a[i+k]
            if k % 2 == 0:
                takahashi += p
            else:
                aoki += p
        if aoki >= ans_a:
            ans_t = max(ans_t, takahashi)
            ans_a = max(ans_a, aoki)
print(ans_t)
