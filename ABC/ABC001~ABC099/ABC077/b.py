N = int(input())
ans = 1
for i in range(N):
    if i * i <= N:
        ans = max(i * i, ans)
    else:
        break
print(ans)
