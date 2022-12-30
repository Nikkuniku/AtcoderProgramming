from collections import Counter
n = int(input())

c = Counter()
for _ in range(n):
    a, b = map(int, input().split())
    c[a] += 1
    c[a+b] -= 1

ans = [0]*(n+1)
days = sorted(c.keys())
cnt = 0
prev_day = 0
curr_day = 0
for d in days:
    ans[cnt] += d-prev_day
    cnt += c[d]
    prev_day = d
print(*ans[1:])
