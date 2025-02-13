N = int(input())
ans = 0
for k in range(1, int(N**0.5) + 1):
    ans += k * (N // k - N // (k + 1))
for i in range(1, N // (int(N**0.5) + 1) + 1):
    ans += N // i
print(ans)
