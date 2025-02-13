N = int(input())
ans = 0
for i in range(60):
    if N % 2 == 0:
        N //= 2
        ans += 1
    else:
        break
print(ans)
