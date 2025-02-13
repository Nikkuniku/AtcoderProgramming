N = int(input())
ans = 0
for i in range(60):
    if N & (1 << i):
        break
    ans += 1
print(ans)
