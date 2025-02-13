N = int(input())
A = list(map(int, input().split()))
cnt = 0
total = 0
for a in A:
    if a > 0:
        cnt += 1
        total += a

ans = (total + cnt - 1) // cnt
print(ans)
