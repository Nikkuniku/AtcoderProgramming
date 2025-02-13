L, R = map(int, input().split())
N = R
lpf = [-1] * (N + 1)
for i in range(2, N + 1):
    j = i
    while j < N + 1:
        if lpf[j] == -1:
            lpf[j] = i
        j += i
ans = 0
for g in range(2, R + 1):
    l = max(2, -(-L // g))
    r = (R // g) + 1
    sigma = [0] * (r + 1)
    sigma_square = [0] * (r + 1)
    for i in range(l, r):
        sigma[lpf[i]] += 1
    tmp = sum(sigma)
    for i in range(l, r):
        ans += sigma[i] * (tmp - sigma[i])
        tmp -= sigma[i]
ans *= 2
print(ans)
