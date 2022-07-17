n = int(input())
p = 1


cnt = [0]*31
for i in range(2, n+1):
    tmp = [0]*31
    j = 2
    while i > 1:
        if i % j == 0:
            i //= j
            tmp[j] += 1
        else:
            j += 1
    for k in range(31):
        cnt[k] = max(cnt[k], tmp[k])
ans = 1
for k, v in enumerate(cnt):
    ans *= pow(k, v)
print(ans+1)
