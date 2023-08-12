H, A = map(int, input().split())
slimes = 1
ans = 0
while H > 0:
    ans += slimes
    H //= A
    slimes *= 2
print(ans)
