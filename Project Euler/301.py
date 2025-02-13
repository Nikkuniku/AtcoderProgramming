ans = 0
for n in range(1, (1 << 30) + 1):
    ans += n ^ (2 * n) ^ (3 * n) == 0
print(ans)
