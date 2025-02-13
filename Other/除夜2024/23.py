N = int(input())
ans = 0
while N > 0:
    if N % 2 == 0:
        ans += 1
        N //= 2
    else:
        break
print(ans)
